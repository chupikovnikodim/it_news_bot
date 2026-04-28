import requests
import os

TOKEN = os.getenv("TG_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")

url = f"https://newsapi.org/v2/everything?q=IT OR AI OR backend&language=en&sortBy=publishedAt&pageSize=5&apiKey={NEWS_API_KEY}"

news = requests.get(url).json()
articles = news.get("articles", [])

if not articles:
    print("Немає новин або помилка API:", news)  # для дебагу в Actions logs
    exit()

message = "📰 IT новини:\n\n"
for a in articles:
    message += f"{a['title']}\n{a['url']}\n\n"

requests.post(
    f"https://api.telegram.org/bot{TOKEN}/sendMessage",
    data={"chat_id": CHAT_ID, "text": message}
)
