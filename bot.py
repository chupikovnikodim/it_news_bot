import requests
import os

OPENAI_KEY = os.getenv("OPENAI_KEY")
TG_TOKEN = os.getenv("TG_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

def get_news():
    response = requests.post(
        "https://api.openai.com/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {OPENAI_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "gpt-4.1-mini",
            "messages": [
                {"role": "user", "content": "Дай короткий IT-дайджест за сьогодні для розробника"}
            ]
        }
    )
    return response.json()["choices"][0]["message"]["content"]

def send_telegram(text):
    requests.post(
        f"https://api.telegram.org/bot{TG_TOKEN}/sendMessage",
        data={"chat_id": CHAT_ID, "text": text}
    )

if __name__ == "__main__":
    news = get_news()
    send_telegram(news)
