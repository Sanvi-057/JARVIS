import requests
from config import GNEWS_API_KEY
from utils.logger import log_action
def get_news():
    country = input("Enter country code (e.g., in, us, gb): ").strip().lower()
    url = (
        f"https://gnews.io/api/v4/top-headlines"
        f"?country={country}"
        f"&lang=en"
        f"&max=5"
        f"&apikey={GNEWS_API_KEY}"
    )

    try:
        response = requests.get(url, timeout=5)
        if response.status_code != 200:
            print(f"\nError: {response.status_code}")
            print(response.text)
            return
        data = response.json()
        if "articles" not in data:
            print("\nNo articles found.")
            print(data)
            return
        articles = data["articles"]
        if not articles:
            print("\nNo news available.")
            return
        print("\n" + "=" * 80)
        print("TOP HEADLINES")
        print("=" * 80)
        for i, article in enumerate(articles, start=1):
            print(f"\n{i}. {article['title']}\n")
            print(f"   Source      : {article['source']['name']}")
            print(f"   Published   : {article['publishedAt']}")
            print(f"   Description : {article['description']}")
            print(f"   Read More   : {article['url']}")
            print("\n" + "-" * 80)
        log_action(f"Viewed top news for {country}")
    except requests.exceptions.RequestException:
        print("\nUnable to connect to the news service.")
    except Exception as e:
        print(f"\nUnexpected Error: {e}")