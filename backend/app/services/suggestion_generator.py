from openai import OpenAI
import json

def generate_suggestions(prompt: str, tokens: list, api_key: str):
    client = OpenAI(api_key=api_key)

    token_str = ", ".join([t["text"] for t in tokens])

    system_prompt = (
        "You are a language model optimization expert and your task is to provide optimization suggestions for the user's Prompt.\n"
        "Requirements: Reduce ambiguity, improve control, enhance goal clarity, and make it easier for non-technical users to understand.\n"
        "The user prompt is as follows:\n"
        f"{prompt}\n\n"
        "The following is the syntactic structure (word order) of the prompt:\n"
        f"{token_str}\n\n"
        "Please return 3 concise, specific, and actionable suggestions in the following format:\n"
        "[\"suggestion_1...\", \"suggestion_2...\", \"suggestion_3...\"]"
    )

    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "system", "content": system_prompt}],
            temperature=0.3
        )
        return json.loads(response.choices[0].message.content)
    except Exception as e:
        print("❌ GPT wrong create answer：", e)
        return []
