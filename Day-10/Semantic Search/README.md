### Extension Task: Search Evaluation Metrics

To quantitatively evaluate the Hybrid Search Engine, a small ground-truth benchmark dataset was created. Two Information Retrieval metrics were implemented:

1. **Mean Reciprocal Rank (MRR)**
   - Measures how quickly the first relevant document appears.
   - Higher values indicate better ranking quality.

2. **Normalized Discounted Cumulative Gain (NDCG)**
   - Measures ranking quality while considering document positions.
   - Rewards placing relevant documents higher in the result list.

The hybrid retrieval system (BM25 + Dense Embeddings + Reciprocal Rank Fusion) was evaluated against six benchmark queries and achieved measurable ranking performance using these standard Information Retrieval metrics.