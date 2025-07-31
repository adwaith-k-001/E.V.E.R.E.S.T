# monitor_memory.py

import time
import os

print("🧠 Memory monitor is running...")

while True:
    os.system("cls" if os.name == "nt" else "clear")
    print("🧠 Monitoring: Retrieved Memory Log\n")

    try:
        with open("monitor_log.txt", "r", encoding="utf-8") as f:
            print(f.read())
    except FileNotFoundError:
        print("monitor_log.txt not found. Has the assistant been run yet?")
    except Exception as e:
        print(f"[ERROR]: {e}")

    time.sleep(3)
