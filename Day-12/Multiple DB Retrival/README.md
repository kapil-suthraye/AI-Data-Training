# Multi-DB Retrieval Showdown

## Overview
This notebook compares three retrieval approaches used in Retrieval-Augmented Generation (RAG):

- FAISS (in-memory vector search)
- Pinecone Serverless (managed vector database)
- Azure AI Search (Hybrid BM25 + Vector Search)

It benchmarks retrieval quality, latency, metadata filtering, hybrid search, and re-ranking.

## Features
- Build embeddings using Sentence Transformers
- Create a FAISS vector index
- Store and retrieve vectors from Pinecone
- Configure Azure AI Search with HNSW vector search
- Hybrid retrieval using BM25 + Vector Search (RRF)
- Cohere Re-ranking evaluation
- Recall and latency benchmarking
- Visualization of p50 and p95 latency metrics

## Tech Stack
- Python
- LangChain
- FAISS
- Pinecone
- Azure AI Search
- Cohere
- Hugging Face Embeddings
- Pandas & Matplotlib

## Learning Outcomes
- Compare exact vs approximate nearest-neighbor search
- Understand hybrid retrieval architectures
- Evaluate retrieval quality using Recall and MRR
- Analyze latency trade-offs across vector databases
- Apply metadata filtering and re-ranking techniques

## Files
- `Multi_DB_Retrival.ipynb` – Main notebook containing all experiments and benchmarks.

## Usage
1. Configure API keys.
2. Install dependencies.
3. Build embeddings and indexes.
4. Run retrieval benchmarks.
5. Compare latency and quality metrics.
6. Review visualizations and conclusions.

## Conclusion
- FAISS is ideal for local experimentation and small datasets.
- Pinecone simplifies production-scale vector search.
- Azure AI Search excels when hybrid keyword + semantic retrieval is required.
- Cohere Re-rank can improve result relevance at the cost of additional latency.
