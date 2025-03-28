import time
from bs4 import Comment
from .utils import get_soup, load_config

config = load_config()


# 获取新闻列表
def fetch_articles(limit=3):
    headers = config.get("headers", {})
    base_url = config["crawler"]["football_italia_milan_url"]

    soup = get_soup(base_url, headers=headers)
    article_soup = soup.find_all("article")

    articles = []

    for article in article_soup[:limit]:
        h4_tag = article.find("h4")
        if not (h4_tag and h4_tag.a):
            continue

        title = h4_tag.get_text(strip=True)
        link = h4_tag.a["href"]

        content = fetch_article_content(link, headers)

        articles.append({"title": title, "url": link, "content": content})

        time.sleep(1)

    return articles


# 利用注释块提取文章正文
def get_content_from_article(soup, marker="Article Start"):
    comments = soup.find_all(string=lambda text: isinstance(text, Comment))
    for comment in comments:
        if marker in comment:
            content_html = comment.find_next_siblings()
            content_paragraphs = [
                tag.get_text(strip=True) for tag in content_html if tag.name == "p"
            ]
            return "\n".join(content_paragraphs)
    return None


# 获取单篇文章正文
def fetch_article_content(url, headers):
    try:
        detail_soup = get_soup(url, headers=headers)
        content = get_content_from_article(detail_soup)

        if not content:
            return "⚠️ 正文注释块未找到"
        return content
    except Exception as e:
        return f"⚠️ 请求失败: {e}"
