import requests
import os
import xml.etree.ElementTree as ET

TOKEN = os.getenv("TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

RSS_URL = "https://dou.ua/lenta/feed/"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36"
}

response = requests.get(RSS_URL, headers=headers, timeout=10)
print(response.status_code)
print(response.text[:300])  # залиш для дебагу, потім можна прибрати

root = ET.fromstring(response.content)
items = root.findall("./channel/item")[:5]

message = "📰 IT новини з DOU:\n\n"
for item in items:
    title = item.findtext("title", "")
    link = item.findtext("link", "")
    message += f"*{title}*\n{link}\n\n"

result = requests.post(
    f"https://api.telegram.org/bot{TOKEN}/sendMessage",
    data={"chat_id": CHAT_ID, "text": message, "parse_mode": "Markdown"}
)
print(result.json())
