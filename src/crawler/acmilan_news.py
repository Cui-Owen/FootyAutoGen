import requests
from bs4 import BeautifulSoup
from .utils import get_soup, load_config

config = load_config()


def fetch_articles(skip=0, limit=10):
    headers = config.get("headers", {})
    base_url = config["crawler"]["acmilan_news_url"]

    params = {
        "order": "elements.publication_date[desc]",
        "skip": skip,
        "limit": limit,
        "language": "italian",
        "system.language": "italian",
        "elements.platform[contains]": "web",
        "system.type": "news",
    }

    response = requests.get(base_url, params=params, headers=headers)
    response.raise_for_status()
    data = response.json()

    articles = []

    for item in data.get("items", []):
        elements = item.get("elements", {})
        title = elements.get("title", {}).get("value", "")
        share_url = elements.get("share_url", {}).get("value", "")
        publication_date = elements.get("publication_date", {}).get("value", "")

        # 抓取详情页 HTML 正文
        content = fetch_article_content(share_url) if share_url else ""

        articles.append(
            {
                "title": title,
                "url": share_url,
                "date": publication_date,
                "content": content,
            }
        )

    return articles


def fetch_article_content(url):
    """访问详情页并提取正文文本"""
    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")

        container = soup.find(
            "div", class_=lambda c: c and c.startswith("WebEditorialElement__Container")
        )

        if not container:
            return "(No article body found)"

        # 只提取 <p> 段落文本，保持整洁
        paragraphs = container.find_all("p")
        text = "\n\n".join(p.get_text(strip=True) for p in paragraphs)

        return text.strip()

    except Exception as e:
        return f"(Failed to fetch content: {e})"


if __name__ == "__main__":
    news = fetch_articles(limit=3)
    for article in news:
        print(f"📰 {article['title']}")
        print(f"🔗 {article['url']}")
        print(f"📄 正文预览:\n{article['content'][:200]}...\n{'-' * 60}")
