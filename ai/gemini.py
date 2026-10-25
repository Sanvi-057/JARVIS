
import os
import re
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key) if api_key else None


# ---------------- GEMINI AI ----------------

def generate_response(prompt, conversation_history=None):
    if client is None:
        return "Gemini API key not found. Please check your .env file."

    history_text = ""

    if conversation_history:
        history_text = "\n".join(
            f"{item[0]}: {item[1]}"
            for item in conversation_history
        )

    full_prompt = f"""
You are Jarvis, a helpful AI desktop assistant.

Previous conversation:
{history_text}

User's current message:
{prompt}

Answer directly and naturally. Avoid unnecessary introductions.
"""

    try:
        response = client.models.generate_content(
            model="gemini-3-flash-preview",
            contents=full_prompt
        )

        return response.text or "I couldn't generate a response."

    except Exception as e:
        print(f"Gemini error: {e}")
        return "I'm having trouble connecting to Gemini right now."


def ask_gemini(prompt, conversation_history=None):
    if conversation_history is None:
        conversation_history = []

    response = generate_response(prompt, conversation_history)

    conversation_history.append(("User", prompt))
    conversation_history.append(("Jarvis", response))

    return response


# ---------------- COMMAND DETECTION ----------------

def detect_command(user_input):
    text = user_input.lower().strip()
    text = re.sub(r"[^\w\s']", "", text)
    text = re.sub(r"\s+", " ", text)

    # Ignore requests that clearly cancel an action
    negative_phrases = [
        "don't open", "do not open", "dont open",
        "don't launch", "do not launch", "dont launch",
        "don't start", "do not start", "dont start",
        "don't run", "do not run", "dont run",
    ]

    if any(phrase in text for phrase in negative_phrases):
        return "NONE"

    # Remove polite wording
    fillers = [
        "please", "can you", "could you", "would you",
        "will you", "for me", "jarvis"
    ]

    for phrase in fillers:
        text = text.replace(phrase, " ")

    text = re.sub(r"\s+", " ", text).strip()

    # Applications
    apps = {
        "google chrome": "open chrome",
        "chrome": "open chrome",
        "visual studio code": "open vscode",
        "vs code": "open vscode",
        "vscode": "open vscode",
        "calculator": "open calculator",
        "notepad": "open notepad",
        "file explorer": "open file explorer",
    }

    actions = ["open", "launch", "start", "run"]

    for app_name, intent in apps.items():
        if (
            app_name in text
            and any(action in text for action in actions)
        ):
            return intent

    # Websites
    if "youtube" in text and any(action in text for action in actions):
        return "open youtube"

    if "github" in text and any(action in text for action in actions):
        return "open github"

    if "google" in text and any(action in text for action in actions):
        return "search google"

    # Time
    if any(phrase in text for phrase in [
        "what time", "current time", "time right now",
        "tell me the time"
    ]):
        return "current time"

    # Date
    if any(phrase in text for phrase in [
        "what is the date", "what's the date",
        "current date", "today's date", "what day is it"
    ]):
        return "current date"

    # Dice
    if any(phrase in text for phrase in [
        "roll dice", "roll a dice", "roll the dice"
    ]):
        return "roll dice"

    # Coin
    if any(phrase in text for phrase in [
        "toss coin", "toss a coin", "flip coin", "flip a coin"
    ]):
        return "toss coin"

    # Weather
    if "weather" in text:
        return "weather"

    # News
    if any(phrase in text for phrase in [
        "top news", "latest news", "headlines"
    ]):
        return "top news"

    # Screenshot
    if "screenshot" in text:
        return "take screenshot"

    # System information
    if any(phrase in text for phrase in [
        "system information", "system info", "computer information"
    ]):
        return "system information"

    # Password generation
    if any(phrase in text for phrase in [
        "generate password", "create password", "make a password"
    ]):
        return "generate password"

    # Notes
    if any(word in text.split() for word in [
        "note", "notes", "notebook"
    ]):
        return "note"

    # File manager
    if any(phrase in text for phrase in [
        "file manager", "manage files"
    ]):
        return "file"

    # Direct folder-opening requests
    folder_phrases = {
        "desktop": ["desktop"],
        "downloads": ["downloads", "download folder"],
        "documents": ["documents", "document folder"],
        "pictures": ["pictures", "picture folder"],
        "videos": ["videos", "video folder"],
    }

    if any(word in text.split() for word in ["open", "show", "go"]):
        for folder, phrases in folder_phrases.items():
            if any(phrase in text for phrase in phrases):
                return f"open {folder}"

    return "NONE"
