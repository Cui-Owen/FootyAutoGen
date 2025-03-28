import requests
from bs4 import BeautifulSoup
import openai
import yaml
import re
from pathlib import Path


def load_config():
    """
    加载 config/config.yaml 并返回配置信息字典
    """
    config_path = Path(__file__).resolve().parents[2] / "config" / "config.yaml"
    with config_path.open("r", encoding="utf-8") as f:
        config = yaml.safe_load(f)
    return config


def fetch_espn_article(url: str):
    """
    从ESPN网站抓取新闻，返回(标题, 正文文本)。
    这里仅作示例，需根据实际网页结构做调整
    """
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/121.0.0.0 Safari/537.36"
        )
    }

    response = requests.get("https://www.espn.com/soccer/", headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "lxml")
        print(soup.title.text)
    else:
        print(f"请求失败，状态码: {response.status_code}")

    title = soup.title.text
    content = soup.find("div", class_="article-body").text

    return title, content


fetch_espn_article("https://www.espn.com/soccer/")
