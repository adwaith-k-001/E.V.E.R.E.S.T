import os
from datetime import datetime

# Pricing for Gemini 1.5 Flash (in USD per 1K tokens)
PRICE_PER_1K_INPUT = 0.000125
PRICE_PER_1K_OUTPUT = 0.000375
USD_TO_INR = 83  # Update as needed

LOG_FILE = "Logs/usage_log.txt"
TOTAL_FILE = "Logs/usage_total.txt"

def log_token_usage(prompt_tokens: int, response_tokens: int):
    total_tokens = prompt_tokens + response_tokens

    # === Cost calculation ===
    cost_usd = (
        (prompt_tokens / 1000) * PRICE_PER_1K_INPUT +
        (response_tokens / 1000) * PRICE_PER_1K_OUTPUT
    )
    cost_inr = round(cost_usd * USD_TO_INR, 4)

    # === Log this session ===
    now = datetime.now()
    timestamp = now.strftime("[%Y-%m-%d %H:%M:%S]")
    log_line = (
        f"{timestamp} Prompt: {prompt_tokens}, Response: {response_tokens}, "
        f"Total: {total_tokens}, Cost: ₹{cost_inr}\n"
    )

    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(log_line)

    # === Load existing totals if present ===
    total_prompt = prompt_tokens
    total_response = response_tokens
    total_cost = cost_inr

    if os.path.exists(TOTAL_FILE):
        with open(TOTAL_FILE, "r", encoding="utf-8") as f:
            lines = f.readlines()
            try:
                total_prompt += int(lines[0].split(":")[1].strip())
                total_response += int(lines[1].split(":")[1].strip())
                total_cost += float(lines[3].split("₹")[1].strip())
            except:
                pass  # Ignore if format is broken

    total_combined = total_prompt + total_response

    # === Write updated totals in human-readable format ===
    with open(TOTAL_FILE, "w", encoding="utf-8") as f:
        f.write(f"Total Prompt Tokens: {total_prompt}\n")
        f.write(f"Total Response Tokens: {total_response}\n")
        f.write(f"Total Tokens: {total_combined}\n")
        f.write(f"Total Cost (INR): ₹{round(total_cost, 4)}\n")
