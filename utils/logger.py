from datetime import datetime
import os


def log_action(action):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    log_file = os.path.join(base_dir, "logs", "jarvis.log")

    with open(log_file, "a") as file:
        file.write(f"[{current_time}] {action}\n")