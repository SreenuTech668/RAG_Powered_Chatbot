# RAG_Powered_Chatbot
RAG-powered chat bot build for the students who are confusing about reading in pdf , it helps to students to make easier to learn
A RAG-Powered PDF Chatbot is an AI application that allows users to upload PDF documents and ask questions in natural language. The chatbot uses Retrieval-Augmented Generation (RAG) to extract relevant information from the PDF and generate accurate, context-aware answers using a Large Language Model (LLM).

The system works by:

Uploading and reading PDF documents.
Splitting the content into smaller text chunks.
Converting the chunks into vector embeddings using embedding models.
Storing the embeddings in a vector database like FAISS or ChromaDB.
Retrieving the most relevant content based on the user’s query.
Sending the retrieved context to an LLM such as Groq models or OpenAI models to generate intelligent responses.

This approach improves answer accuracy by grounding the AI’s responses in the uploaded document instead of relying only on general knowledge. RAG-powered PDF chatbots are widely used for:

Document analysis
Research assistance
Customer support
Legal and medical document querying
Educational learning systems
Enterprise knowledge management


# RAG-Powered Chat Intelligence

## Overview

RAG-Powered Chat Intelligence is an AI-driven document question-answering system built using Retrieval-Augmented Generation (RAG). Users can upload documents and ask questions in natural language. The system retrieves relevant information from the uploaded documents and generates accurate responses using a Large Language Model (LLM).

A key feature of this project is its ability to prevent hallucinations by responding with **"Not Found in Document"** whenever the requested information is unavailable in the uploaded content.

---

## Features

- Upload PDF, DOCX, or TXT documents
- Extract and process document content
- Create vector embeddings for semantic search
- Retrieve relevant document chunks
- Generate context-aware answers using an LLM
- Return "Not Found in Document" when information is unavailable
- User-friendly chat interface
- Observability and monitoring using Langfuse
- Streamlit-based frontend

---

## System Architecture

### Workflow

1. User uploads a document.
2. Document text is extracted.
3. Text is split into chunks.
4. Embeddings are generated for each chunk.
5. Embeddings are stored in a vector database.
6. User asks a question.
7. Similar chunks are retrieved from the vector database.
8. Retrieved context is passed to the LLM.
9. LLM generates an answer.
10. If no relevant context is found, the system returns:
    - **"Not Found in Document"**

**Document Upload**
→ Text Extraction
→ Text Chunking
→ Embedding Generation
→ Vector Database Storage
→ User Question
→ Query Embedding
→ Similarity Search
→ Context Found?
    ├─ Yes → Retrieve Chunks → LLM → Generate Answer
    └─ No  → Not Found in Document
→ Display Response
→ Langfuse Monitoring                ↓
Langfuse Monitoring
(Traces, Tokens, Latency, Cost)

**Technology Stack**
Frontend
Streamlit
Backend
Python
LangChain
Vector Database
FAISS / ChromaDB
LLM
OpenAI GPT Models
Gemini Models (Optional)
Monitoring
Langfuse
Document Processing
PyPDF
Docx
Text Loaders
