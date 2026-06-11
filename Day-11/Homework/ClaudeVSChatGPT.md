# Claude vs ChatGPT Prompt Structure

| Aspect | ChatGPT Prompt Structure | Claude Prompt Structure |
|----------|--------------------------|--------------------------|
| Preferred Style | Flexible, conversational, instruction-driven | Structured, XML/tag-based, context-heavy |
| System Instructions | Works well with role + task definitions | Strongly benefits from explicit constitutional-style instructions |
| Delimiters | Triple backticks (```), markdown sections | XML tags (`<task>`, `<context>`, `<instructions>`) preferred |
| Context Handling | Handles mixed context effectively | Performs better when context is clearly separated |
| Few-Shot Examples | Helpful but not always required | Often improves significantly with examples |
| Chain of Thought | Can follow step-by-step reasoning requests | Excels when reasoning steps are explicitly structured |
| Long Documents | Good context handling | Generally stronger with very large context windows |
| Output Control | Strong through explicit formatting instructions | Strong through structured schemas and tags |
| JSON Generation | Reliable with schema definitions | Reliable when output format is clearly specified |
| Prompt Complexity | Handles simple prompts well | Benefits from highly organized prompts |
| Best Practice | Role → Task → Constraints → Output Format | Context → Instructions → Constraints → Output Format |
| Error Reduction | Explicit rules and examples | Explicit tags and detailed constraints |

---

# Recommended ChatGPT Prompt Template

```text
Role:
You are a Senior Data Scientist.

Task:
Analyze the attached dataset and identify trends.

Requirements:
1. Calculate summary statistics.
2. Detect missing values.
3. Generate visualizations.
4. Provide business insights.

Output Format:
- Executive Summary
- Analysis
- Visualizations
- Recommendations
```

---

# Recommended Claude Prompt Template

```xml
<context>
Attached dataset contains sales transactions from 2025.
</context>

<task>
Analyze the dataset and identify trends.
</task>

<requirements>
1. Calculate summary statistics.
2. Detect missing values.
3. Generate visualizations.
4. Provide business insights.
</requirements>

<output_format>
- Executive Summary
- Analysis
- Visualizations
- Recommendations
</output_format>
```

---

# Rule of Thumb

| If Using... | Recommended Structure |
|------------|----------------------|
| ChatGPT | Role → Task → Constraints → Output Format |
| Claude | Context → Task → Requirements → Output Format (preferably with XML tags) |
| Both Models | Goal → Context → Instructions → Constraints → Examples → Output Format |

**Universal Prompt Formula (works well for both):**

```text
Goal
↓
Context
↓
Instructions
↓
Constraints
↓
Examples (optional)
↓
Expected Output Format
```