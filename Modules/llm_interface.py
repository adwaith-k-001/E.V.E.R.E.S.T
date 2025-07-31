# modules/llm_interface.py

import google.generativeai as genai
from Modules.usage_tracker import log_token_usage  # ← Token tracking integration

# === Direct Gemini API Key and Model Name ===
GEMINI_API_KEY = "AIzaSyBFhKWQYRsmQ5YgHWsgnU41ZbtUpzMqwGA"  # Replace with your real key
DEFAULT_MODEL = "gemini-1.5-flash"  # or "gemini-pro"

# Configure Gemini
genai.configure(api_key=GEMINI_API_KEY)

# Load the model
model = genai.GenerativeModel(DEFAULT_MODEL)

def get_llm_response(prompt: str) -> str:
    try:
        response = model.generate_content(prompt)

        # === Extract token usage and log it ===
        usage = getattr(response, "usage_metadata", None)
        if usage:
            prompt_tokens = getattr(usage, "prompt_token_count", 0)
            response_tokens = getattr(usage, "candidates_token_count", 0)
            log_token_usage(prompt_tokens, response_tokens)
        else:
            print("[⚠️] Token usage metadata not available.")

        return response.text.strip() if hasattr(response, "text") else "[ERROR]: No response text."

    except Exception as e:
        return f"[ERROR]: {str(e)}"
