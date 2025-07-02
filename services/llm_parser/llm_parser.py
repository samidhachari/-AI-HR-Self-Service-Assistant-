import openai
openai.api_key = "YOUR_API_KEY"

def extract_intent(text):
    prompt = f"""
    You are an HR assistant. Extract intent and return JSON:
    Query: "{text}"
    """
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content