import subprocess
import os

def open_chrome():
    print("Opening Chrome...")
    subprocess.Popen(r"C:\Program Files\Google\Chrome\Application\chrome.exe")


def open_vscode():
    vscode_path = os.path.join(
        os.path.expanduser("~"),
        "AppData",
        "Local",
        "Programs",
        "Microsoft VS Code",
        "Code.exe"
    )
    subprocess.Popen(vscode_path)


def open_calculator():
    print("Opening Calculator...")
    subprocess.Popen("calc")


def open_notepad():
    print("Opening Notepad...")
    subprocess.Popen("notepad")


def open_file_explorer():
    print("Opening File Explorer...")
    subprocess.Popen("explorer")