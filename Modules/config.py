# modules/config.py

import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY") or "your-api-key-here"
DEFAULT_MODEL = "gemini-pro"
