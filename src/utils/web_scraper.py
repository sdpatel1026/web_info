import requests
from bs4 import BeautifulSoup

def fetch_homepage(url: str) -> str:
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, "html.parser")
        all_text=""
        for text in soup.stripped_strings:
            all_text += text 
        return all_text
    except requests.RequestException as e:
        raise ValueError(f"Error fetching URL: {e}")
