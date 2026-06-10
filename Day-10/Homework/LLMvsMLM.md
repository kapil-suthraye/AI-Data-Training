### LLM vs MLM

| Feature | LLM (Large Language Model) | MLM (Masked Language Model) |
|----------|----------------------------|-----------------------------|
| Purpose | Generate and understand text | Predict masked/missing words |
| Training Objective | Next-token prediction | Masked-token prediction |
| Input | Sequential text | Text with masked tokens |
| Output | Generates complete text | Fills masked words |
| Context Usage | Uses previous tokens only (causal) | Uses both left and right context |
| Text Generation | Excellent | Not designed for free-form generation |
| Architecture | Decoder-based Transformer | Encoder-based Transformer |
| Example Models | GPT, LLaMA, Gemini | BERT, RoBERTa, ALBERT |
| Typical Tasks | Chatbots, summarization, coding, content generation | Classification, sentiment analysis, NER, search |
| Training Example | "The cat sat on the ___" → predicts next word | "The cat [MASK] on the mat" → predicts "sat" |

**Summary:** LLMs are designed for text generation by predicting the next token, whereas MLMs learn language understanding by predicting masked words using context from both directions.