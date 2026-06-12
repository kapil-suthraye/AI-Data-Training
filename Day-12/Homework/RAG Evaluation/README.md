# Simple RAG Evaluation Demo using Groq

## Overview

This project demonstrates a simple Retrieval-Augmented Generation (RAG) evaluation workflow using Groq LLMs without relying on Ragas or other evaluation frameworks.

The notebook evaluates generated responses using three commonly used RAG metrics:

* **Context Relevance** – Measures whether the retrieved context is relevant to the user's question.
* **Answer Relevance** – Measures whether the generated answer addresses the user's question.
* **Groundedness (Faithfulness)** – Measures whether the generated answer is supported by the retrieved context.

The evaluation is performed by using a Groq-hosted LLM as an automated judge.

---

## Technologies Used

* Python
* Google Colab
* Groq API
* LangChain
* Pandas
* Matplotlib

---

## Project Workflow

1. Configure Groq API credentials.
2. Create sample RAG evaluation data.
3. Generate metric-specific evaluation prompts.
4. Use Groq LLM to score:

   * Context Relevance
   * Answer Relevance
   * Groundedness
5. Store evaluation results in a Pandas DataFrame.
6. Visualize scores using bar charts.

---

## Sample Evaluation Results

| Question                      | Context Relevance | Answer Relevance | Groundedness |
| ----------------------------- | ----------------- | ---------------- | ------------ |
| What is FAISS?                | 5                 | 5                | 4            |
| What is BM25?                 | 5                 | 4                | 5            |
| What is FAISS? (Hallucinated) | 5                 | 1                | 1            |

### Interpretation

* High Context Relevance indicates successful retrieval.
* High Answer Relevance indicates the response answers the question.
* High Groundedness indicates the answer is supported by the retrieved context.
* Low Groundedness often indicates hallucination.

---

## Visualization

The notebook generates charts to compare:

* Context Relevance
* Answer Relevance
* Groundedness

across multiple questions and responses.

---

## Learning Outcomes

This demo helps understand:

* Basic RAG evaluation concepts
* Hallucination detection
* Faithfulness assessment
* LLM-as-a-Judge evaluation patterns
* Visualization of RAG performance metrics

---

## Future Enhancements

* Add larger evaluation datasets
* Compare multiple LLMs
* Integrate vector databases such as Pinecone or FAISS
* Add automated benchmarking pipelines
* Export evaluation reports

---

## Note

This project is intended for educational and demonstration purposes and provides a lightweight alternative to framework-based evaluation solutions.
