import pyautogui
import time
import datetime
import os

from utils.logger import log_action

def take_ss():

    print("Screenshot will be taken in 5 seconds...")
    time.sleep(5)

    # Show current working directory
    print("Current Working Directory:")
    print(os.getcwd())

    # Create screenshots folder if it doesn't exist
    os.makedirs("screenshot", exist_ok=True)

    # Generate filename
    current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"screenshot/screenshot_{current_time}.png"

    # Take screenshot
    screenshot = pyautogui.screenshot()

    # Save screenshot
    screenshot.save(filename)

    # Debug information
    print("\nScreenshot saved successfully!")
    print(f"Relative Path : {filename}")
    print(f"Absolute Path : {os.path.abspath(filename)}")
    print(f"File Exists   : {os.path.exists(filename)}")

    log_action(f"Screenshot saved: {filename}")

    '''import pyautogui
import time
import datetime
import os #Whenever you want to work with:foldersfilespathsenvironment variables

from utils.logger import log_action

def take_ss():
    print("Screenshot will be taken in 5 seconds...")
    time.sleep(5)#paauses the program n gives time to swtch
    os.makedirs("screenshots", exist_ok=True)# creates a folder  n exist just dont cash when there isnt any file
    current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"screenshots/screenshot_{current_time}.png"#screenshots/ means saved inside ss folder
    screenshot = pyautogui.screenshot()
    screenshot.save(filename)
    print(f"Screenshot saved successfully!")
    print(f"Location: {filename}")
    log_action(f"Screenshot saved: {filename}")'''
