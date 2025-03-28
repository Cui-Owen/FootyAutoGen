import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
# 现有的导入
from src.storage.database import engine, Base
from src.storage.models import Article


def init():
    Base.metadata.create_all(bind=engine)
    print("✅ 数据库初始化完成！")


if __name__ == "__main__":
    init()
