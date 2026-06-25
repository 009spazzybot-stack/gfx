import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "sqlite:///bot.db"
)

OPENAI_KEY = os.getenv("OPENAI_KEY")

GOOGLE_KEY = os.getenv("GOOGLE_KEY")
GOOGLE_CX = os.getenv("GOOGLE_CX")
