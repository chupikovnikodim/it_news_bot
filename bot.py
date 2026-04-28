import requests
import os

OPENAI_KEY = os.getenv("OPENAI_API_KEY")

def get_news():
    url = "https://api.openai.com/v1/responses"

    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "gpt-4.1-mini",
        "input": "Дай короткий IT-дайджест за сьогодні для розробника"
    }

    response = requests.post(url, headers=headers, json=data)

    result = response.json()

    print(result)

    return result["output"][0]["content"][0]["text"]
