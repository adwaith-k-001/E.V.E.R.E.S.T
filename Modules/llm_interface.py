# modules/llm_interface.py

import google.generativeai as genai

# === Direct Gemini API Key and Model Name ===
GEMINI_API_KEY = "AIzaSyCFJDSWLGtxnaFSo7jOevCW5cdrUngo_v8"  # Replace with your real key
DEFAULT_MODEL = "gemini-1.5-flash"  # or "gemini-pro"

# Configure Gemini
genai.configure(api_key=GEMINI_API_KEY)

# Load the model
model = genai.GenerativeModel(DEFAULT_MODEL)

def get_llm_response(prompt: str) -> str:
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"[ERROR]: {str(e)}"
