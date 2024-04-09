import os
import pathlib
from dotenv import load_dotenv

load_dotenv(".env")

DISCORD_SECRET_TOKEN = os.getenv("DISCORD_BOT_TOKEN")

BASE_DIR = pathlib.Path(__file__).parent
COMMANDS_DIR = BASE_DIR / "commands"