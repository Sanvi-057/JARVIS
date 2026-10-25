import os
print(os.getcwd())
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
from utils.logger import log_action
from commands.weather_commands import get_weather
from commands.news_commands import get_news
from commands.screenshot_commands import take_ss
from commands.system_commands import system_info
from commands.notes_commands import notes
from commands.file_commands import file_manager
from ai.router import route_command
from voice.voice_input import listen


def display_menu():
    print("\n====================================")
    print("          JARVIS LITE")
    print("====================================")
    print("1. Open Chrome")
    print("2. Open VS Code")
    print("3. Open Calculator")
    print("4. Open Notepad")
    print("5. Open File Explorer")
    print("6. Search Google")
    print("7. Open YouTube")
    print("8. Open GitHub")
    print("9. Current Time")
    print("10. Current Date")
    print("11. Generate Password")
    print("12. Roll Dice")
    print("13. Toss Coin")
    print("14. weather")
    print("15. Top News")
    print("16. Take Screenshot")
    print("17. System Information")
    print("18. Note")
    print("19. file")
    print("20. Command Mode (Beta)")
    print("2_. Exit")
    print("====================================")

commands = {
    "1": open_chrome,
    "2": open_vscode,
    "3": open_calculator,
    "4": open_notepad,
    "5": open_file_explorer,
    "6": search_google,
    "7": open_youtube,
    "8": open_github,
}

while True:
    display_menu()
    choice = input("Choose an option: ")
    if choice == "9":
        print("Current Time:", current_time())
        log_action("Checked Current Time")
    elif choice == "10":
        print("Current Date:", current_date())
        log_action("Checked Current Date")
    elif choice == "11":
        try:
            length = int(input("Enter password length (4-50): "))
            if 4 <= length <= 50:
                print("Generated Password:", generate_password(length))
                log_action("Generated Password")
            else:
                print("Password length must be between 4 and 50.")
        except ValueError:
            print("Please enter a valid number.")
    elif choice == "12":
        dice=roll_dice()
        print("You rolled:", roll_dice())
        log_action(f"Rolled Dice: {dice}")
    elif choice == "13":
        coin=toss_coin()
        print("Result:", toss_coin())
        log_action(f"Tossed Coin: {coin}")
    elif choice == "14":
        get_weather()
    elif choice == "15":
        get_news()
        log_action("Viewed Top News")
    elif choice == "16":
        take_ss()
    elif choice == "17":
        system_info()
    elif choice == "18":
        notes()
    elif choice == "19":
        file_manager()


    elif choice == "20":
        print("\n==============================")
        print("       JARVIS VOICE MODE")
        print("Say 'Jarvis, wake up' to activate.")
        print("Say 'go to sleep' to deactivate.")
        print("Say 'exit' to return to the menu.")
        print("==============================")

        conversation_history = []
        is_awake = False

        while True:
            command = listen()

            if not command:
                continue

            command = command.lower().strip()
            print("You said:", command)

            # Exit voice mode completely
            if command == "exit":
                print("Leaving Jarvis Voice Mode...")
                break

            # Waiting for the wake phrase
            if not is_awake:
                if "jarvis" in command and (
                    "wake up" in command or "wake" in command
                ):
                    is_awake = True
                    print("Jarvis: I'm online. How can I help?")
                else:
                    print("Jarvis is sleeping. Say 'Jarvis, wake up'.")
                continue

            # Put Jarvis back to sleep
            if "go to sleep" in command or command == "sleep":
                is_awake = False
                print("Jarvis: Going to sleep. Call me when you need me.")
                continue

            # Process commands while awake
            response = route_command(command, conversation_history)

            if response:
                print(f"Jarvis: {response}")




    elif choice == "2_":
        log_action("Exited Jarvis")
        print("Goodbye!")
        break
    elif choice in commands:
        commands[choice]()
        actions = {
        "1": "Opened Chrome",
        "2": "Opened VS Code",
        "3": "Opened Calculator",
        "4": "Opened Notepad",
        "5": "Opened File Explorer",
        "6": "Searched Google",
        "7": "Opened YouTube",
        "8": "Opened GitHub",
        }

        log_action(actions[choice])
    else:
        print("Invalid option! Please try again.")
