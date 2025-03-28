from crawler.football_italia import fetch_articles as fetch_football_italia
from crawler.acmilan_news import fetch_articles as fetch_acmilan_news
from processor.translator import Translator
from storage.database import get_db_session
from storage.models import Article


def main():
    translator = Translator()
    articles = fetch_football_italia(limit=3)

    with next(get_db_session()) as db:
        for article in articles:
            chinese_summary = translator.translate_and_summarize(article["content"])

            # 检查数据库是否已存在该URL
            existing = db.query(Article).filter_by(url=article["url"]).first()
            if existing:
                print(f"⚠️ 已存在文章，跳过: {article['title']}")
                continue

            # 创建新文章记录
            new_article = Article(
                source="football_italia",
                title=article["title"],
                url=article["url"],
                english_content=article["content"],
                chinese_summary=chinese_summary,
            )
            db.add(new_article)
            print(f"✅ 已保存文章到数据库: {article['title']}")

        db.commit()


if __name__ == "__main__":
    main()
