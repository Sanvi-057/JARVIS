import random
import string

def generate_password(length=12):
    characters = (
        string.ascii_letters
        + string.digits
        + string.punctuation
    )
    password = ""
    for _ in range(length):
        password += random.choice(characters)
    return password