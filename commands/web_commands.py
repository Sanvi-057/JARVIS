import webbrowser

def search_google():
    query = input("Enter what you want to search: ")
    webbrowser.open(f"https://www.google.com/search?q={query}")


def open_youtube():
    webbrowser.open("https://www.youtube.com")


def open_github():
    webbrowser.open("https://github.com")