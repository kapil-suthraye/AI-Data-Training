# Hybrid RAG with Long Context

A simple implementation of a **Hybrid Retrieval-Augmented Generation (RAG)** system that combines semantic and keyword-based retrieval techniques with Long Context Large Language Models (LLMs) for improved question answering and knowledge retrieval.

## 🚀 Project Overview

This notebook demonstrates how Hybrid RAG can enhance retrieval accuracy by combining multiple search strategies and providing relevant context to an LLM for answer generation.

The project also includes evaluation techniques to measure retrieval quality, answer relevance, groundedness, and hallucination detection.

## ✨ Features

* Hybrid Retrieval (Dense + Sparse Search)
* Long Context Processing
* Retrieval-Augmented Generation (RAG)
* Context-Aware Question Answering
* Hallucination Detection
* Groundedness Evaluation
* Retrieval Performance Analysis

## 🛠️ Tech Stack

* Python
* FAISS
* Azure AI Search / BM25
* LangChain
* Groq LLM
* Jupyter Notebook

## 📋 Workflow

1. Load and preprocess documents
2. Build retrieval indexes
3. Perform hybrid search
4. Retrieve relevant context
5. Generate answers using an LLM
6. Evaluate answer quality and grounding

## 📊 Outcome

The implementation demonstrates that combining dense and sparse retrieval methods with long-context LLMs can improve answer relevance, reduce hallucinations, and provide more reliable responses for enterprise knowledge retrieval use cases.

## 📁 File

* `Hybrid_RAG_LongContext.ipynb` – Complete implementation of the Hybrid RAG pipeline.

## 🎯 Learning Objectives

* Understand Hybrid RAG architecture
* Compare retrieval strategies
* Evaluate RAG system performance
* Analyze answer groundedness and hallucinations
* Work with long-context LLM applications

---

**Author:** Kapil Suthraye
**Purpose:** Learning and experimentation with Hybrid RAG and Long Context AI systems.
