import requests
import os
import xml.etree.ElementTree as ET

TOKEN = os.getenv("TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

RSS_URL = "https://feeds.feedburner.com/TheHackersNews"

response = requests.get(RSS_URL, timeout=10)
root = ET.fromstring(response.content)

items = root.findall("./channel/item")[:5]

message = "📰 IT новини:\n\n"
for item in items:
    title = item.findtext("title", "")
    link = item.findtext("link", "")
    message += f"*{title}*\n{link}\n\n"

result = requests.post(
    f"https://api.telegram.org/bot{TOKEN}/sendMessage",
    data={"chat_id": CHAT_ID, "text": message, "parse_mode": "Markdown"}
)

print(result.json())  # для дебагу в логах
