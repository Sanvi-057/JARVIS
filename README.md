# JARVIS Lite — AI Desktop Assistant

JARVIS Lite is a Python-based desktop assistant designed to make everyday computer tasks easier through voice commands and a menu-driven interface.

## Features

- **Voice Control:** Interact with Jarvis using spoken commands.
- **AI Chat:** Get responses to general questions using Google's Gemini API.
- **Application Launcher:** Open applications such as Chrome, VS Code, Calculator, and Notepad.
- **Web Access:** Open websites and perform Google searches.
- **System Information:** Check basic system details.
- **Utilities:** Access time, date, dice rolls, and coin tosses.
- **Weather and News:** Retrieve weather information and top news.
- **File Management:** Create files and folders and open common directories.
- **Password Generator:** Generate random passwords.
- **Notes and Screenshots:** Manage notes and capture screenshots.

## Technologies Used

- Python
- Google Gemini API
- SpeechRecognition
- SoundDevice and NumPy
- Requests
- PyAutoGUI
- Psutil

## Setup Instructions

1. Clone or download this repository.
2. Install the required dependencies:

   ```bash
   python -m pip install -r requirements.txt
   ```

3. Create a `.env` file in the project root and add your Gemini API key:

   ```env
   GEMINI_API_KEY=your_gemini_api_key
   ```

4. Add any other API keys required by your weather and news modules, using the variable names defined in `config.py`.
5. Run the assistant:

   ```bash
   python main.py
   ```

## Project Structure

- `ai/` — AI responses and command routing
- `commands/` — Desktop, web, utility, and system commands
- `voice/` — Voice input and speech recognition
- `utils/` — Helper utilities and password generation
- `data/` — Application data
- `logs/` — Application logs
- `main.py` — Main application entry point

## Security

API keys and other secrets should remain in your local `.env` file. Never commit this file to GitHub.

## Status

Version 1.0 is under development. Features and documentation may change as the project evolves.
