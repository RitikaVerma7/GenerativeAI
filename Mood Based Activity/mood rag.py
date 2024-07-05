import streamlit as st
import os
import re
from PyPDF2 import PdfReader
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.retrievers import MultiQueryRetriever
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain

from secret_key import my_openapi_key

# Set your OpenAI API key
os.environ['OPENAI_API_KEY'] = my_openapi_key

# Load OpenAI model
llm = OpenAI(model_name="gpt-3.5-turbo-instruct", temperature=0.6)

# Helper functions
def get_pdf_text(pdf_files):
    text = ""
    for pdf_file in pdf_files:
        pdf_reader = PdfReader(pdf_file)
        for page in pdf_reader.pages:
            text += page.extract_text()
    cleaned_text = re.sub(r'\s+', ' ', text)  # Replace multiple whitespace with a single space
    return cleaned_text

def get_text_chunks_with_metadata(text, source, page_number=None):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=100)
    chunks = text_splitter.split_text(text)
    chunk_metadata = [{"source": source, "page_number": page_number, "chunk_index": i} for i, chunk in enumerate(chunks)]
    return list(zip(chunks, chunk_metadata))

def get_vectorstore(text_chunks_with_metadata):
    embeddings = OpenAIEmbeddings()
    texts = [text for text, metadata in text_chunks_with_metadata]
    metadatas = [metadata for text, metadata in text_chunks_with_metadata]
    vectorstore = FAISS.from_texts(texts=texts, embedding=embeddings, metadatas=metadatas)
    return vectorstore

def get_conversation_chain(vectorstore):
    llm = ChatOpenAI(temperature=0)
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
    QUERY_PROMPT = PromptTemplate(template="You are a helpful assistant. Your task is to generate five different versions of the given user {question} to retrieve relevant documents from a vector database. Please provide variations of the query: {question} to retrieve relevant documents from a vector database. By generating multiple perspectives on the user question, your goal is to help the user overcome some of the limitations of the distance-based similarity search. Also, you need to stick to the context only. If there any other query outside the document just answer politely to the user to ask questions relevant to the context.", input_variables=["question"])
    llm_chain = LLMChain(llm=llm, prompt=QUERY_PROMPT)
    retriever = MultiQueryRetriever.from_llm(vectorstore.as_retriever(), llm, prompt=QUERY_PROMPT)
    conversation_chain = ConversationalRetrievalChain.from_llm(llm=llm, retriever=retriever, memory=memory)
    return conversation_chain

def generate_activity_recommendation(mood):
    prompt_template = PromptTemplate(
        input_variables=['mood'],
        template="You are a helpful assistant. Give a line for emotional acknowledgment and then suggest 7 activities, explaining them in 2-3 lines, I shall do based on my {mood}."
    )
    recommendation_chain = LLMChain(llm=llm, prompt=prompt_template)
    response = recommendation_chain.invoke({'mood': mood})
    
    if response and 'text' in response:
        return response['text'].strip()
    else:
        st.error("Failed to generate activity recommendation. Check API response.")
        return ""

# Streamlit app interface
st.title('Mood-Based Activity Recommender')
st.markdown("""
    <style>
    .main { background-color: #f0f2f6; }
    .stTextInput { border-radius: 5px; }
    .stButton button { background-color: #4CAF50; color: white; border-radius: 5px; }
    </style>
    """, unsafe_allow_html=True)

# Text input for mood
mood = st.text_input("Enter your mood:", placeholder="e.g., happy, sad, stressed")

# File uploader for PDF
uploaded_files = st.file_uploader("Upload PDF files", type=["pdf"], accept_multiple_files=True)

# Button to generate response
if st.button("Generate Activity"):
    if mood:
        activity = generate_activity_recommendation(mood)
        st.markdown(f"**Suggested Activities:**\n{activity}")
    else:
        st.warning("Please enter your mood.")

# Process PDF files
if uploaded_files:
    pdf_text = get_pdf_text(uploaded_files)
    text_chunks_with_metadata = get_text_chunks_with_metadata(pdf_text, source="Mood and Activity Recommendation Dataset")
    vectorstore = get_vectorstore(text_chunks_with_metadata)
    conversation_chain = get_conversation_chain(vectorstore)
    
    st.markdown("PDF content has been processed and vector store has been created.")

# Footer
st.markdown("""
    <hr>
    <div style='text-align: center;'>
        <small>Empowering you with the right activities. Enhance your mood!</small>
    </div>
    """, unsafe_allow_html=True)
