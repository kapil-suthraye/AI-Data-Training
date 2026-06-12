# HealthBot: Clinical RAG Architecture

## High-Level Architecture

```text
                ┌──────────────────────┐
                │  Clinician Portal    │
                │  Web / Mobile App    │
                └──────────┬───────────┘
                           │
                           ▼
                ┌──────────────────────┐
                │ API Gateway          │
                │ Authentication       │
                │ Audit Logging        │
                └──────────┬───────────┘
                           │
                           ▼
                ┌──────────────────────┐
                │ Query Router         │
                │ Domain Detection     │
                └──────────┬───────────┘
                           │
       ┌───────────────────┼───────────────────┐
       │                   │                   │
       ▼                   ▼                   ▼

┌────────────────┐ ┌────────────────┐ ┌────────────────┐
│ Cardiology     │ │ Oncology       │ │ Drug Index     │
│ Hybrid Search  │ │ Hybrid Search  │ │ Hybrid Search  │
└───────┬────────┘ └───────┬────────┘ └───────┬────────┘
        │                  │                  │
        └──────────┬───────┴───────┬──────────┘
                   ▼
      ┌──────────────────────────────┐
      │ Hybrid Retrieval Layer       │
      │ BM25 + Vector Search         │
      └──────────────┬───────────────┘
                     ▼
      ┌──────────────────────────────┐
      │ Semantic Reranker            │
      │ Top-K Optimization           │
      └──────────────┬───────────────┘
                     ▼
      ┌──────────────────────────────┐
      │ Context Builder              │
      │ Parent Chunk Reconstruction  │
      └──────────────┬───────────────┘
                     ▼
      ┌──────────────────────────────┐
      │ Claude / GPT                 │
      │ Grounded Generation          │
      └──────────────┬───────────────┘
                     ▼
      ┌──────────────────────────────┐
      │ Clinical Response            │
      │ + Citations                  │
      │ + Confidence Score           │
      └──────────────┬───────────────┘
                     ▼
      ┌──────────────────────────────┐
      │ Audit Store                  │
      │ Compliance Logs              │
      └──────────────────────────────┘
```

---

# Document Ingestion Pipeline

```text
Clinical Guidelines
Drug Databases
Hospital Protocols
Research Papers
Internal SOPs
        │
        ▼
┌──────────────────────┐
│ Document Collection  │
└──────────┬───────────┘
           ▼
┌──────────────────────┐
│ OCR / Parsing        │
└──────────┬───────────┘
           ▼
┌──────────────────────┐
│ Metadata Extraction  │
└──────────┬───────────┘
           ▼
┌──────────────────────┐
│ Parent Chunking      │
│ 1024 Tokens          │
└──────────┬───────────┘
           ▼
┌──────────────────────┐
│ Child Chunking       │
│ 256 Tokens           │
└──────────┬───────────┘
           ▼
┌──────────────────────┐
│ Embedding Generation │
└──────────┬───────────┘
           ▼
┌──────────────────────┐
│ Azure AI Search      │
│ Multi-Index Storage  │
└──────────────────────┘
```

---

# Retrieval Workflow

```text
User Query
    │
    ▼
Domain Classification
    │
    ▼
Target Index Selection
    │
    ▼
Hybrid Search
(BM25 + Vector)
    │
    ▼
Top-K Results
    │
    ▼
Semantic Reranker
    │
    ▼
Parent Chunk Recovery
    │
    ▼
Context Assembly
    │
    ▼
LLM Generation
    │
    ▼
Grounded Response
    │
    ▼
Citations + Confidence Score
```

---

# Recommended Azure Services

| Layer | Service |
|---------|---------|
| Frontend | React / Angular |
| API Layer | Azure API Management |
| Authentication | Azure Entra ID |
| Retrieval | Azure AI Search |
| Embeddings | Azure OpenAI Embedding Models |
| LLM | GPT-4o / Claude |
| Storage | Azure Blob Storage |
| Monitoring | Azure Monitor |
| Logging | Azure Log Analytics |
| Security | Azure Key Vault |
| Audit | Azure SQL / Cosmos DB |

---

# Enterprise Enhancements

## Caching Layer

Use Redis Cache for:

- Frequently asked clinical queries
- Drug interaction lookups
- Guideline summaries

Expected latency reduction:

- 30–50%

---

## Human Escalation

If confidence score < threshold:

1. Flag response
2. Notify specialist
3. Route to human review

---

## Observability

Monitor:

- Retrieval latency
- Generation latency
- Groundedness score
- Hallucination rate
- User satisfaction
- Token consumption

---

# Expected Outcomes

- <3s End-to-End Latency
- >92% Clinical Accuracy
- HIPAA Compliance
- High Availability
- Enterprise Scalability
- Full Auditability
- Reduced Hallucinations