## Project Description
Developed an end-to-end AI-powered application that enables users to interact conversationally with multiple documents across various formats — including PDFs, presentations, images, and text files.

The system leverages Retrieval-Augmented Generation (RAG) to provide accurate, context-aware answers by converting documents into vector embeddings and performing semantic search.

Users can upload multiple research papers or files simultaneously and ask detailed questions, receiving intelligent responses grounded in the document content.

---

## Key Features

- **Multi-Document Support**
  - Upload and process multiple files at once (PDF, PPT, TXT, JPG, PNG, MD)

- **Semantic Search with FAISS**
  - Efficient vector-based retrieval for relevant context

- **OCR for Images**
  - Extracts text from images using Tesseract for deeper analysis

- **Fast & Scalable Processing**
  - Handles large files (up to 200MB per document)

- **Modular Architecture**
  - Clean separation of document parsing, chunking, embedding, and retrieval

- **Local Vector Storage**
  - Uses FAISS indexing for quick and offline retrieval

---

## System Architecture

- **Document Ingestion**
  - Upload files (PDF, PPT, images, text)

- **Text Extraction**
  - Extract content using format-specific libraries

- **Text Chunking**
  - Split into smaller chunks for better embedding

- **Embedding Generation**
  - Convert text into vectors using embedding models

- **Vector Storage (FAISS)**
  - Store embeddings for fast similarity search

- **Query Processing (RAG)**
  - Retrieve relevant chunks → pass to LLM → generate answer

---

## Tech Stack

### Frontend
- Streamlit (Interactive web UI)

### Backend & AI/ML
- Python 3.11
- Google Gemini Pro (LLM)
- LangChain (LLM orchestration framework)
- LangChain-Google-GenAI

### Document Processing
- PyPDF2 (PDF parsing)
- python-pptx (presentation handling)
- Pillow (image processing)
- pytesseract (OCR)
- RecursiveCharacterTextSplitter (chunking)

### Vector Database
- FAISS (Facebook AI Similarity Search)
- Google Generative AI Embeddings

### Environment Management
- python-dotenv
- OS environment variables (API keys)