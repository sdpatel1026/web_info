from src.utils.web_scraper import fetch_homepage
from src.utils.llm import analyze_content

def web_info(url: str) -> dict:
    # Fetch the homepage content
    try:
        content = fetch_homepage(url)
        # print("content:",content)
        # Analyze the content using LangChain + OpenAI
        return analyze_content(content)
    except Exception as e:
        raise e
