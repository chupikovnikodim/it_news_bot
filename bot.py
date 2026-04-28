import requests
import os
import xml.etree.ElementTree as ET

TOKEN = os.getenv("TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

def translate_to_ua(text):
    url = "https://translate.googleapis.com/translate_a/single"
    params = {
        "client": "gtx",
        "sl": "en",
        "tl": "uk",
        "dt": "t",
        "q": text
    }
    r = requests.get(url, params=params)
    return r.json()[0][0][0]

RSS_URL = "https://techcrunch.com/feed/"
response = requests.get(RSS_URL, timeout=10)
root = ET.fromstring(response.content)
items = root.findall("./channel/item")[:5]

message = "📰 IT новини:\n\n"
for item in items:
    title = item.findtext("title", "")
    link = item.findtext("link", "")
    translated = translate_to_ua(title)
    message += f"*{translated}*\n{link}\n\n"

result = requests.post(
    f"https://api.telegram.org/bot{TOKEN}/sendMessage",
    data={"chat_id": CHAT_ID, "text": message, "parse_mode": "Markdown"}
)
print(result.json())
