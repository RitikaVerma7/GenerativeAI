import streamlit as st
import os
from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from secret_key import my_openapi_key

# Set your OpenAI API key
os.environ['OPENAI_API_KEY'] = my_openapi_key 

# Load OpenAI model
llm = OpenAI(model_name="gpt-3.5-turbo-instruct", temperature=0.6)

def generate_activity_recommendation(mood):
    prompt_template = PromptTemplate(
        input_variables=['mood'],
        template="You are a helpful assistant. Give a line for emotional acknoledgement and then Suggest me 7 activities I shall do based on my {mood}?"
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

# Button to generate response
if st.button("Generate Activity"):
    if mood:
        activity = generate_activity_recommendation(mood)
        st.markdown(f"**Suggested Activities:**\n{activity}")
    else:
        st.warning("Please enter your mood.")

# Footer
st.markdown("""
    <hr>
    <div style='text-align: center;'>
        <small>Empowering you with the right activities. Enhance your mood!</small>
    </div>
    """, unsafe_allow_html=True)
