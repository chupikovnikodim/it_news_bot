import requests
import os

TOKEN = os.getenv("TG_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
API_KEY = os.getenv("OPENAI_API_KEY")

url = f"https://newsapi.org/v2/everything?q=IT OR AI OR backend OR fullstack&language=en&sortBy=publishedAt&pageSize=5&apiKey={API_KEY}"

news = requests.get(url).json()

articles = news.get("articles", [])

message = "📰 IT новини:\n\n"

for a in articles:
    message += f"{a['title']}\n{a['url']}\n\n"

requests.post(
    f"https://api.telegram.org/bot{TOKEN}/sendMessage",
    data={"chat_id": CHAT_ID, "text": message}
)
