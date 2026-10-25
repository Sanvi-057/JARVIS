from commands.app_commands import (
    open_chrome,
    open_vscode,
    open_calculator,
    open_notepad,
    open_file_explorer,
)
from commands.web_commands import (
    search_google,
    open_youtube,
    open_github,
)

from commands.utility_commands import (
    current_time,
    current_date,
    roll_dice,
    toss_coin,
)

from utils.password_generator import generate_password
from commands.weather_commands import get_weather
from commands.news_commands import get_news
from commands.screenshot_commands import take_ss
from commands.system_commands import system_info
from commands.notes_commands import notes
from commands.file_commands import (
    file_manager,
    open_folder,
    create_desktop_file,
    create_desktop_folder,
)

from ai.gemini import ask_gemini


COMMAND_MAP = {
    #Applications
    "open chrome": open_chrome,
    "open vscode": open_vscode,
    "open calculator": open_calculator,
    "open notepad": open_notepad,
    "open file explorer": open_file_explorer,

    #Web
    "search google": search_google,
    "open youtube": open_youtube,
    "open github": open_github,

    # Utilities
    "current time": current_time,
    "current date": current_date,
    "generate password": generate_password,
    "roll dice": roll_dice,
    "toss coin": toss_coin,

    # Information
    "weather": get_weather,
    "top news": get_news,

    # System
    "take screenshot": take_ss,
    "system information": system_info,

    # Personal tools
    "note": notes,
    "file": file_manager,
        # Voice file and folder commands
    "open desktop": lambda: open_folder("desktop"),
    "open downloads": lambda: open_folder("downloads"),
    "open documents": lambda: open_folder("documents"),
    "open pictures": lambda: open_folder("pictures"),
    "open videos": lambda: open_folder("videos"),

}