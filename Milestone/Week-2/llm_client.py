import os

from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def generate_summary(text, style, model, max_tokens):

    if style == "brief":
        prompt = f"""
Summarize into exactly 2 bullet points.
Each bullet maximum 20 words.

{text}
"""
    else:
        prompt = f"""
Provide detailed summary in 3 paragraphs.

{text}
"""

    response = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        max_tokens=max_tokens
    )

    return response.choices[0].message.content