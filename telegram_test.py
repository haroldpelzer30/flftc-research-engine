from dotenv import load_dotenv
import os
import requests

load_dotenv()

bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
chat_id = os.getenv("TELEGRAM_CHAT_ID")

message = "🚀 FlightDeck Telegram test successful!"

url = f"https://api.telegram.org/bot{bot_token}/sendMessage"

response = requests.post(
    url,
    data={
        "chat_id": chat_id,
        "text": message
    }
)

print(response.status_code)
print(response.text)