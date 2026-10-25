from datetime import datetime
import random

def current_time():
    """Return the current time."""
    now = datetime.now()
    return now.strftime("%I:%M:%S %p")


def current_date():
    """Return the current date."""
    now = datetime.now()
    return now.strftime("%d-%m-%Y")


def roll_dice():
    """Return a random number between 1 and 6."""
    return random.randint(1, 6)


def toss_coin():
    """Return Heads or Tails randomly."""
    return random.choice(["Heads", "Tails"])