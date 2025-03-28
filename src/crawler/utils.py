import requests
from bs4 import BeautifulSoup, Comment


def get_soup(url, headers):
    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()
    return BeautifulSoup(response.content, "lxml")


def extract_content_from_comments(soup, marker="Article Start"):
    comments = soup.find_all(string=lambda text: isinstance(text, Comment))
    for comment in comments:
        if marker in comment:
            content_html = comment.find_next_siblings()
            content_paragraphs = [
                tag.get_text(strip=True) for tag in content_html if tag.name == "p"
            ]
            return "\n".join(content_paragraphs)
    return None
