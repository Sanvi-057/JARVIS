import os
from utils.logger import log_action

# Common Paths
home = os.path.expanduser("~")
desktop = os.path.join(home, "Desktop")
downloads = os.path.join(home, "Downloads")
documents = os.path.join(home, "Documents")
pictures = os.path.join(home, "Pictures")
videos = os.path.join(home, "Videos")


def file_manager():

    print("\n==========================")
    print("      FILE MANAGER")
    print("==========================")

    print("1. Create Folder")
    print("2. Create File")
    print("3. Open Desktop")
    print("4. Open Downloads")
    print("5. Open Documents")
    print("6. Open Pictures")
    print("7. Open Videos")

    choice = input("\nChoose an option: ")

    if choice == "1":

        folder_name = input("Enter folder name: ").strip()
        folder_path = os.path.join(desktop, folder_name)
        if os.path.exists(folder_path):
            print("Folder already exists.")
        else:
            os.makedirs(folder_path)
            print("Folder created successfully.")
            log_action(f"Created folder: {folder_name}")

    elif choice == "2":

        file_name = input("Enter file name: ").strip()
        if not file_name.endswith(".txt"):
            file_name += ".txt"
        file_path = os.path.join(desktop, file_name)
        if os.path.exists(file_path):
            print("File already exists.")
        else:
            with open(file_path, "w") as file:
                pass
            print("File created successfully.")
            log_action(f"Created file: {file_name}")

    elif choice == "3":

        os.startfile(desktop)
        print("Opening Desktop...")
        log_action("Opened Desktop.")

    elif choice == "4":

        os.startfile(downloads)
        print("Opening Downloads...")
        log_action("Opened Downloads.")

    elif choice == "5":

        os.startfile(documents)
        print("Opening Documents...")
        log_action("Opened Documents.")

    elif choice == "6":

        os.startfile(pictures)
        print("Opening Pictures...")
        log_action("Opened Pictures.")

    elif choice == "7":

        os.startfile(videos)
        print("Opening Videos...")
        log_action("Opened Videos.")

    else:
        print("Invalid Choice.")


def open_folder(folder_name):
    folders = {
        "desktop": desktop,
        "downloads": downloads,
        "documents": documents,
        "pictures": pictures,
        "videos": videos,
    }

    path = folders.get(folder_name.lower().strip())

    if not path:
        return "I don't recognize that folder."

    if not os.path.isdir(path):
        return f"The {folder_name} folder wasn't found."

    os.startfile(path)
    log_action(f"Opened {folder_name.title()}")
    return f"Opening {folder_name.title()}."


def create_desktop_file(file_name):
    file_name = os.path.basename(file_name.strip())

    if not file_name:
        return "Please provide a file name."

    if file_name in (".", ".."):
        return "That file name isn't allowed."

    if not file_name.lower().endswith(".txt"):
        file_name += ".txt"

    file_path = os.path.join(desktop, file_name)

    if os.path.exists(file_path):
        return "A file with that name already exists on your Desktop."

    try:
        with open(file_path, "x", encoding="utf-8"):
            pass

        log_action(f"Created file: {file_name}")
        return f"Created {file_name} on your Desktop."

    except OSError as e:
        return f"I couldn't create the file: {e}"


def create_desktop_folder(folder_name):
    folder_name = folder_name.strip()

    if not folder_name or folder_name in (".", ".."):
        return "Please provide a valid folder name."

    if os.path.basename(folder_name) != folder_name:
        return "Please provide only a folder name, not a path."

    folder_path = os.path.join(desktop, folder_name)

    try:
        os.mkdir(folder_path)
        log_action(f"Created folder: {folder_name}")
        return f"Created the folder {folder_name} on your Desktop."

    except FileExistsError:
        return "A file or folder with that name already exists."

    except OSError as e:
        return f"I couldn't create the folder: {e}"
