# HealthBot: Clinical RAG at Enterprise Scale

## Scenario

A large hospital network requires an AI assistant for 3,000 clinicians capable of answering questions from over 2 million pages of:

- Clinical guidelines
- Drug interaction databases
- Internal hospital protocols
- Research documents

### Key Requirements

- End-to-end latency < 3 seconds
- Answer accuracy > 92%
- HIPAA compliant
- Azure data residency
- Enterprise-scale deployment

---

# Architecture Decisions

## 1. Azure AI Search (Hybrid) vs Weaviate on AKS

### Recommendation: Azure AI Search Hybrid Retrieval

| Criteria | Azure AI Search | Weaviate on AKS |
|-----------|----------------|----------------|
| HIPAA Compliance | Yes | Requires additional controls |
| Security | Managed | Self-managed |
| Operations | Low overhead | Cluster maintenance required |
| Hybrid Search | Native support | Supported |
| Governance | Strong | Custom implementation |
| Flexibility | Moderate | High |

### Decision

Use Azure AI Search because:

- Easier HIPAA compliance
- Managed infrastructure
- Integrated security controls
- Reduced operational complexity
- Native hybrid retrieval

---

## 2. Chunk Size Strategy

### Challenge

Clinical documents contain:

- Long paragraphs
- Medical terminology
- Tables
- Drug dosage information
- Contraindications

### Recommendation: Parent-Child Chunking

Parent Chunk:
- 1024 tokens

Child Chunks:
- 256 tokens

Example:

1024-token Parent Chunk
├── Child Chunk 1 (256)
├── Child Chunk 2 (256)
├── Child Chunk 3 (256)
└── Child Chunk 4 (256)

### Benefits

- Better retrieval precision
- Preserves document context
- Improved grounding
- Reduced hallucinations

---

## 3. Claude Long Context vs Traditional RAG

### Recommendation

Use both approaches.

### Use RAG For

- Guideline lookup
- Drug interaction checks
- Protocol retrieval
- Medical fact verification

### Use Claude + RAG For

- Multi-document reasoning
- Clinical workflow analysis
- Cross-domain recommendations

### Why Not Skip RAG?

Clinical information changes frequently.

Without retrieval:

- Hallucination risk increases
- Outdated information may be generated
- No source traceability

Clinical systems require:

- Grounded answers
- Source citations
- Auditability

---

## 4. Single Index vs Multi-Index

### Recommendation

Domain-Based Multi-Index Architecture

Indexes:

- Cardiology
- Oncology
- Neurology
- Radiology
- Drug Interactions
- Internal Protocols

### Benefits

- Faster retrieval
- Better relevance
- Reduced search space
- Easier governance

---

## 5. Retrieval Strategy

### Hybrid Retrieval

Combine:

1. BM25 Search
2. Vector Search
3. Semantic Reranking

### Why Hybrid?

Clinical queries often contain:

- Medical codes
- Drug names
- Exact terminology

BM25 captures:

- Exact keyword matches

Vector Search captures:

- Semantic meaning

Reranker improves:

- Final relevance ordering

---

## 6. Compliance and Governance

### HIPAA Requirements

- Azure-only deployment
- Encryption at rest
- Encryption in transit
- Role-based access control
- Audit logging
- Data residency controls

### Audit Requirements

Store:

- User query
- Retrieved documents
- Generated answer
- Model version
- Confidence score

---

# Final Recommendation

- Azure AI Search Hybrid Retrieval
- Parent (1024) + Child (256) Chunking
- Domain-Based Multi-Index Strategy
- BM25 + Vector Retrieval
- Cross-Encoder Reranking
- Claude/GPT with RAG
- Mandatory Citations
- HIPAA-Compliant Azure Deployment
- Full Audit Trail
- Human Escalation for Low Confidence Responses

Expected Outcomes:

- <3 second latency
- >92% answer accuracy
- Enterprise-scale reliability
- Regulatory compliance