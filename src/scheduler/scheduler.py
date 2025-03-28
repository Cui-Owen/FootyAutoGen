from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
from src.crawler.football_italia import fetch_latest_articles
from src.processor.translator import Translator
from src.storage.database import get_db_session
from src.storage.models import Article
import logging

logging.basicConfig(
    filename="logs/scheduler.log",
    format="%(asctime)s %(levelname)s:%(message)s",
    level=logging.INFO,
)


def fetch_and_store_job():
    logging.info(f"[{datetime.now()}] 🟢 定时任务启动")

    translator = Translator()
    articles = fetch_latest_articles(limit=3)

    with next(get_db_session()) as db:
        for article in articles:
            chinese_summary = translator.translate_and_summarize(article["content"])

            existing = db.query(Article).filter_by(url=article["url"]).first()
            if existing:
                logging.info(f"⚠️ 已存在文章，跳过: {article['title']}")
                continue

            new_article = Article(
                source="football_italia",
                title=article["title"],
                url=article["url"],
                english_content=article["content"],
                chinese_summary=chinese_summary,
            )
            db.add(new_article)
            logging.info(f"✅ 已保存文章到数据库: {article['title']}")

        db.commit()
    logging.info(f"[{datetime.now()}] 🟢 定时任务结束\n")


def run_scheduler():
    scheduler = BlockingScheduler()

    # 每20分钟执行一次（可根据需要调整）
    scheduler.add_job(fetch_and_store_job, "interval", minutes=20)

    logging.info("🟢 调度器启动，定时任务每20分钟执行一次")
    scheduler.start()


if __name__ == "__main__":
    run_scheduler()
