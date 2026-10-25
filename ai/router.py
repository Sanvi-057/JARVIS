
from command_map import COMMAND_MAP
from ai.gemini import ask_gemini, detect_command
from utils.password_generator import generate_password
import re
from commands.file_commands import (
    create_desktop_file,
    create_desktop_folder,
)

def route_command(command, conversation_history):

    intent = detect_command(command)

    text = command.lower().strip()

    # Create a file using its spoken name
    file_match = re.search(
        r"create (?:a )?file called (.+?)(?: on my desktop)?$",
        text
    )

    if file_match:
        file_name = file_match.group(1).strip()
        return create_desktop_file(file_name)

        # Create a file using its spoken name
    file_match = re.search(
        r"create (?:a )?file (?:called|named) (.+?)(?:\s+on (?:my )?desktop)?[.!?]*$",
        command.strip(),
        re.IGNORECASE
    )
    if file_match:
        file_name = file_match.group(1).strip()
        return create_desktop_file(file_name)

    # Create a folder using its spoken name
    folder_match = re.search(
        r"(?:create|make) (?:a )?folder (?:called|named) (.+?)(?:\s+on (?:my )?desktop)?[.!?]*$",
        command.strip(),
        re.IGNORECASE
    )
    if folder_match:
        folder_name = folder_match.group(1).strip()
        return create_desktop_folder(folder_name)
    if intent == "NONE":
        return ask_gemini(command, conversation_history)

    if intent == "generate password":
        try:
            length = int(input("How long should the password be? "))

            if 4 <= length <= 50:
                result = generate_password(length)
                print(result)
            else:
                print("Password length must be between 4 and 50.")

        except ValueError:
            print("Please enter a valid number.")

        return None

    if intent in COMMAND_MAP:
        return COMMAND_MAP[intent]()

    # If a recognized intent has no registered command,
    # use Gemini as a fallback.
    return ask_gemini(command, conversation_history)
