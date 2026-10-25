from utils.logger import log_action
import os
base_dir = os.path.dirname(os.path.dirname(__file__))
notes_path = os.path.join(base_dir, "data", "notes.txt")


def notes():
    print("\n==========================")
    print("         NOTES")
    print("==========================")
    print("1. Write Note")
    print("2. View Notes")
    choice = input("\nChoose an option: ")
    if choice == "1":
        note = input("Enter your note: ")
        with open(notes_path, "a") as file:
            file.write(note + "\n")
        print("Note saved successfully.")
        log_action("Added a new note.")
    elif choice == "2":
        try:
            with open(notes_path, "r") as file:
                notes = file.read()
                if notes.strip() == "":
                    print("No notes found.")
                else:
                    print("\n========== YOUR NOTES ==========")
                    print(notes)
            log_action("Viewed notes.")
        except FileNotFoundError:
            print("No notes found.")
    else:
        print("Invalid Choice.")
