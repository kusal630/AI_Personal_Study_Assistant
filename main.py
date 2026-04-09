from openai import OpenAI
import os
from dotenv import load_dotenv
from tools import generate_quiz, summarize_notes, create_study_plan
from memory import save, get

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def agent(user_input):
    save(user_input)
    context = "\n".join(get())

    # Tool routing (important for assignment)
    if "quiz" in user_input.lower():
        return generate_quiz(user_input)

    elif "plan" in user_input.lower():
        return create_study_plan(user_input)

    elif "summary" in user_input.lower():
        return summarize_notes(user_input)

    # Otherwise use OpenAI
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful study assistant."},
            {"role": "user", "content": f"Context:\n{context}\n\nUser:\n{user_input}"}
        ]
    )

    return {
        "type": "explanation",
        "content": response.choices[0].message.content
    }


if __name__ == "__main__":
    while True:
        user = input("You: ")
        print("AI:", agent(user))