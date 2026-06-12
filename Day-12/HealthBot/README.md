# HealthBot: Clinical RAG Architecture

## Overview

This project presents an enterprise-scale Clinical Retrieval-Augmented Generation (RAG) architecture designed for a large hospital network supporting over 3,000 clinicians and a clinical knowledge base containing more than 2 million pages of medical guidelines, drug interaction data, and internal protocols.

## Task

Design a secure, scalable, and HIPAA-compliant AI assistant capable of:

* Providing accurate clinical answers with source citations
* Maintaining end-to-end response latency under 3 seconds
* Achieving greater than 92% answer accuracy
* Supporting enterprise-scale healthcare operations
* Ensuring full auditability and compliance

## Solution

The proposed architecture leverages:

* Azure AI Search with Hybrid Retrieval (BM25 + Vector Search)
* Parent-Child Chunking Strategy (1024/256 tokens)
* Multi-Index Domain-Based Search
* Semantic Reranking
* Large Language Models (Claude/GPT)
* Citation-Based Grounded Responses
* Azure-Native Security and Compliance Controls

## Outcome

The solution delivers:

* Fast and reliable clinical information retrieval
* Reduced hallucinations through grounded generation
* Improved answer relevance via hybrid search and reranking
* HIPAA-compliant deployment architecture
* Enterprise-grade scalability, monitoring, and audit logging

This documentation includes detailed design decisions, architecture diagrams, ingestion workflows, retrieval pipelines, and recommended Azure services for production deployment.
