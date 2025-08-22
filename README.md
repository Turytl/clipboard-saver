# Clipboard Manager

Automatically saves everything copied to your clipboard.

## Features
- Tracks clipboard changes in real-time.
- Saves timestamped history to `clipboard_history.json`.
- Simple and lightweight, perfect for automation tasks.
- Cross-platform support (Windows, macOS, Linux).

## Installation
1. Clone or download this repository.
2. Install dependencies:
```bash
pip install -r requirements.txt
````

## Usage

Run the script:

```bash
python clipboard_manager.py
```

* Copy text as usual; new items are saved automatically.
* Stop the script with `Ctrl+C`. Clipboard history is preserved.

![usage]("assets/usage.gif")

## File Structure

* `clipboard_manager.py` – main script.
* `clipboard_history.json` – automatically created history file.
* `requirements.txt` – Python dependencies.

## Notes

* Works on macOS, Windows, and Linux.
* Requires Python 3.6+.
