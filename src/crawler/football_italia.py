import time
from pathlib import Path
import yaml
from .utils import get_soup, extract_content_from_comments


# 加载配置
def load_config():
    config_path = Path(__file__).resolve().parents[2] / "config" / "config.yaml"
    with config_path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f)


config = load_config()


# 获取新闻列表
def fetch_latest_articles(limit=3):
    headers = config.get("headers", {})
    base_url = config["crawler"]["football_italia_milan_url"]

    soup = get_soup(base_url, headers=headers)
    articles = soup.find_all("article")

    news_list = []

    for article in articles[:limit]:
        h4_tag = article.find("h4")
        if not (h4_tag and h4_tag.a):
            continue

        title = h4_tag.get_text(strip=True)
        link = h4_tag.a["href"]

        content = fetch_article_content(link, headers)

        news_list.append({"title": title, "url": link, "content": content})

        print(f"✅ 已抓取新闻: {title}")
        time.sleep(1)

    return news_list


# 获取单篇文章正文
def fetch_article_content(url, headers):
    try:
        detail_soup = get_soup(url, headers=headers)
        content = extract_content_from_comments(detail_soup)

        if not content:
            return "⚠️ 正文注释块未找到"
        return content
    except Exception as e:
        return f"⚠️ 请求失败: {e}"
