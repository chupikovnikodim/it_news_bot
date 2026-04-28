import requests

TOKEN = "ТУТ_ТВОЙ_TOKEN"
CHAT_ID = "ТУТ_CHAT_ID"

url = "https://newsapi.org/v2/everything?q=IT OR AI OR backend OR fullstack&language=en&sortBy=publishedAt&pageSize=5&apiKey=ТУТ_API_KEY"

news = requests.get(url).json()

articles = news.get("articles", [])

message = "📰 IT новини:\n\n"

for a in articles:
    message += f"{a['title']}\n{a['url']}\n\n"

requests.post(
    f"https://api.telegram.org/bot{TOKEN}/sendMessage",
    data={"chat_id": CHAT_ID, "text": message}
)
