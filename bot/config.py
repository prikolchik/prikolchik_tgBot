import os
from dotenv import load_dotenv

load_dotenv()

def get_bot_token():
    token = os.getenv("BOT_TOKEN", "").strip()
    if not token:
        raise SystemExit("Токен не найдено в .env")
    return token