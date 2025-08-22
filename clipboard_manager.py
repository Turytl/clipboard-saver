import pyperclip
import time
import json
from datetime import datetime
import os

HISTORY_FILE = "clipboard_history.json"

def load_history():
    if os.path.exists(HISTORY_FILE):
        try:
            with open(HISTORY_FILE, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []
    return []

def save_history(history):
    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f, indent=2)

def main():
    print("Clipboard Manager running... Press Ctrl+C to stop.")
    history = load_history()
    last_clip = ""
    try:
        while True:
            clip = pyperclip.paste()
            if clip != last_clip:
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                entry = {"timestamp": timestamp, "content": clip}
                history.append(entry)
                save_history(history)
                print(f"Saved: {clip[:30]}{'...' if len(clip)>30 else ''}")
                last_clip = clip
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nStopped. Clipboard history saved.")

if __name__ == "__main__":
    main()
