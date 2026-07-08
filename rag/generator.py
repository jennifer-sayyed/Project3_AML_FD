from dotenv import load_dotenv
import os

from openai import OpenAI

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)

def generate_answer(question, docs):

    context = "\n".join(
        [d.page_content for d in docs]
    )

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "user",
                "content": f"""
                Context:
                {context}

                Question:
                {question}
                """
            }
        ]
    )

    return response.choices[0].message.content