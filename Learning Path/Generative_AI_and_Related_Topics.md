
# Generative AI and Related Topics

## 1. Introduction to Generative AI and Large Language Models (LLMs)

### What is Generative AI?
- **Definition**: Generative AI refers to artificial intelligence systems capable of generating new content, such as text, images, or music, based on the data they were trained on.
- **Applications**: Includes chatbots, content creation, music composition, and more.

### Selecting the LLM Model
- **Criteria and Considerations**: Factors include the size of the model, training data, computational requirements, and the specific use case it needs to address.

### Front-End, Back-End, and API Calls
- **Integration Overview**: Understanding how to connect LLMs with user interfaces (front-end) and server-side operations (back-end).
- **API Calls**: Learning to use APIs (Application Programming Interfaces) to interact with LLMs programmatically.

### Custom GPT, GPT Store, and Plugins
- **Customizing GPT**: Tailoring GPT models to meet specific needs or applications.
- **GPT Store**: A marketplace for pre-built GPT models and applications.
- **Plugins**: Additional functionalities that can be integrated into GPT models to enhance their capabilities.

## 2. Prompt Engineering

### Nine Techniques of Prompt Engineering
1. Ask Open-Ended Questions: Frame questions that allow for detailed and expansive answers.
2. Include Details in Queries: Specific details help generate more relevant and accurate responses.
3. Adopt a Persona: Guide the model to respond from a particular perspective or role.
4. Use Delimiters: Clearly mark different sections or components of the input.
5. Specify Steps: Break down tasks into clear, sequential steps for the model.
6. Provide Examples: Show examples to guide the model's responses.
7. Specify Output Length: Control how long the model's output should be.
8. Write Clearly: Ensure the prompt is easily understandable and unambiguous.
9. Instruct Deliberation: Encourage the model to consider its response carefully before answering.

## 3. Vector Database

### Vector Database Fundamentals
- **Definition and Importance**: Vector databases store data as vectors (numerical representations) for efficient similarity searches, which is crucial for handling high-dimensional data like embeddings.
- **Features**:
  - Efficient Similarity Search: Quickly find similar items within large datasets based on vector proximity.

### Working with Vector Databases
- **Key Technologies**:
  - Pinecone: A managed service for vector similarity search.
  - Chroma: An open-source embedding database for AI applications.

## 4. Retrieval-Augmented Generation (RAG)

### RAG Architecture
- **Definition**: RAG combines retrieval-based methods with generative models to enhance the relevance and accuracy of AI-generated content.
- **Components**:
  - Retriever: Fetches relevant documents or information based on a query.
  - Generator: Produces content based on the retrieved information.
- **Applications**: Used in tasks requiring high accuracy and context, such as customer support, research, and detailed content creation.
- **Implementation**: Learn to integrate retrieval mechanisms with generative models to create more informed and contextually accurate outputs.

## 5. Helpful Links
1. [Vectors, tokens, Embedding](https://thenewstack.io/the-building-blocks-of-llms-vectors-tokens-and-embeddings/#:~:text=Embeddings%20are%20high%2Ddimensional%20vectors,generation%2C%20sentiment%20analysis%20and%20more)
2. [Semantic Search Using Embeddings and Vector Databases](https://medium.com/@pankaj_pandey/exploring-semantic-search-using-embeddings-and-vector-databases-with-some-popular-use-cases-2543a79d3ba6)
