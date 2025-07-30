# modules/llm_interface.py

import google.generativeai as genai
from modules.config import GEMINI_API_KEY, DEFAULT_MODEL

# Configure Gemini
genai.configure(api_key=GEMINI_API_KEY)

# Load the model (e.g., "gemini-pro", "gemini-1.5-flash")
model = genai.GenerativeModel(DEFAULT_MODEL)

def get_llm_response(prompt: str) -> str:
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"[ERROR]: {str(e)}"
