import os
from dotenv import load_dotenv
from groq import Groq
from utils.prompts import SYSTEM_PROMPT, USER_TEMPLATE, build_context
from utils.retriever import search_demons

load_dotenv()
_client = Groq(api_key=os.environ["GROQ_API_KEY"])

MODEL = "openai/gpt-oss-120b"

def answer(question: str) -> str:
    hits = search_demons(question, limit=3)

    if not hits:
        # No retrieval hit — still answer, but instruct the model to say it lacks info
        context = "No matching entries found in the knowledge base."
    else:
        context = build_context(hits)

    completion = _client.chat.completions.create(
        model=MODEL,
        temperature=0.2,          # low for factual tone
        max_tokens=800,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user",   "content": USER_TEMPLATE.format(context=context, question=question)},
        ],
    )
    return completion.choices[0].message.content