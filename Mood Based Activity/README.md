# Mood-Based Activity Recommender

Mood-Based Activity Recommender is a web application that provides activity recommendations based on the user's mood. It is built using generative AI technology and runs on Streamlit. The application processes PDF files for enhanced retrieval and utilizes OpenAI's GPT models for generating personalized activity suggestions.

## Features
- Generate personalized activity recommendations based on user mood.
- Upload and process PDF files to extract text and create a vector store.
- Set up a conversational retrieval chain for document interaction.
- Interactive and user-friendly interface with Streamlit.

## Demo
![Demo](https://github.com/yourusername/mood-activity-recommender/demo.gif)

## Tech Stack
- **Streamlit**: Web framework for creating interactive applications.
- **LangChain**: Framework for building applications with language models.
- **OpenAI API**: Language model for generating text and embeddings.
- **FAISS**: Library for efficient similarity search and clustering.
- **PyPDF2**: Library for reading PDF files.


## Usage

1. **Run the Streamlit app**:
    ```bash
    streamlit run app.py
    ```

2. **Input your mood**:
    - Enter your current mood in the text input field (e.g., happy, sad, stressed).

3. **Upload PDF files**:
    - Use the file uploader to upload one or multiple PDF files.

4. **Generate Activity Recommendations**:
    - Click on the "Generate Activity" button to receive tailored activity suggestions based on your mood.

5. **Process PDF Content**:
    - The app will process the uploaded PDF files and create a vector store for document retrieval.

## Code Explanation

### Helper Functions

- **get_pdf_text**: Extracts and cleans text from uploaded PDF files.
- **get_text_chunks_with_metadata**: Splits text into manageable chunks with metadata for context.
- **get_vectorstore**: Creates a vector store from text chunks using FAISS and OpenAI embeddings.
- **get_conversation_chain**: Sets up a conversational retrieval chain for document interaction.

### Main Functions

- **generate_activity_recommendation**: Generates activity recommendations based on the user's mood using OpenAI's GPT model.

### Streamlit Interface

- **Text Input**: Field for entering the user's current mood.
- **File Uploader**: Allows users to upload PDF files for processing.
- **Generate Button**: Generates activity recommendations based on the input mood.
- **PDF Processing**: Displays the status of PDF processing and vector store creation.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.