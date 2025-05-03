from openai import OpenAI
import json

def score_prompt(prompt: str, api_key: str):
    client = OpenAI(api_key=api_key)

    system_prompt = (
        "You are an LLM Prompt scoring expert. Please rate Prompt based on the following five dimensions (1-10) and explain your reasons:\n"
        "1. clarity\n2. control\n3. goal_specificity\n4. ambiguity (the more, the lower the score)\n5. readability\n"
        "Please return in the following JSON format:\n"
        "{ \"clarity\": x, \"control\": x, \"goal_specificity\": x, \"ambiguity\": x, \"readability\": x,\n"
        "  \"reason\": {\"clarity\": \"...\", ...} }"
    )

    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3
        )
        return json.loads(response.choices[0].message.content)
    except Exception as e:
        print("❌ GPT wrong rate：", e)
        raise
