# Smart FAQ Bot using RAG

A simple Retrieval-Augmented Generation (RAG) application that answers FAQ questions using semantic search and a Large Language Model.

## Tech Stack

* Groq (LLM Inference)
* Hugging Face Embeddings
* FAISS Vector Store
* LangChain
* Python

## Architecture

User Query → Embedding → FAISS Similarity Search → Retrieve Top FAQs → Groq LLM → Answer

## Features

* Semantic FAQ retrieval
* Fast vector search using FAISS
* Context-aware answer generation
* Retrieval-Augmented Generation (RAG) workflow
* Simple command-line interface

## Project Structure

```text
smart-faq-bot/
│
├── app.py
├── faq_data.py
├── embeddings.py
├── vector_store.py
├── .env
├── requirements.txt
└── README.md
```

## Installation

### Clone Repository

```bash
git clone <repository-url>
cd smart-faq-bot
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

## Configuration

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key
```

## Running the Application

```bash
python app.py
```

Example:

```text
Ask Question: What is RAG?

Answer:
RAG (Retrieval-Augmented Generation) combines retrieval of relevant information with LLM-based generation to provide accurate responses.
```

## How It Works

1. FAQs are converted into vector embeddings.
2. Embeddings are stored in a FAISS index.
3. User query is converted into an embedding.
4. FAISS retrieves the most relevant FAQs.
5. Retrieved context is passed to the Groq LLM.
6. The LLM generates the final answer.

## Learning Outcomes

* Understanding RAG architecture
* Working with vector databases
* Semantic search implementation
* Prompt engineering
* LLM integration using Groq
* Building AI-powered FAQ systems


## License

This project is intended for learning and educational purposes.
