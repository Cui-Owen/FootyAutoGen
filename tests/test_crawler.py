# tests/test_crawler.py
from crawler.acmilan_news import fetch_articles

news = fetch_articles(limit=3)
for article in news:
    print(f"📰 {article['title']}")
    print(f"🔗 {article['url']}")
    print(f"📄 正文预览:\n{article['content'][:200]}...\n{'-' * 60}")
