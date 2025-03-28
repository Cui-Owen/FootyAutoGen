from sqlalchemy import Column, Integer, String, Text, Boolean, DateTime
from .database import Base
from datetime import datetime


class Article(Base):
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True, autoincrement=True)
    source = Column(String(50), index=True)
    title = Column(String(500), index=True)
    url = Column(Text, unique=True, index=True)
    english_content = Column(Text)
    chinese_summary = Column(Text)
    fetched_at = Column(DateTime, default=datetime.now)
    published = Column(Boolean, default=False)
