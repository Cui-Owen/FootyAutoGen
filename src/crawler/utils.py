import requests
import yaml
from pathlib import Path
from bs4 import BeautifulSoup


def load_config():
    config_path = Path(__file__).resolve().parents[2] / "config" / "config.yaml"
    with config_path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def get_soup(url, headers):
    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()
    return BeautifulSoup(response.content, "lxml")
