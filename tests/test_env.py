import yaml
from pathlib import Path


def load_config():
    """
    加载 config/config.yaml 并返回配置信息字典
    """
    config_path = Path(__file__).resolve().parents[1] / "config" / "config.yaml"
    print("Config path is:", config_path)
    with config_path.open("r", encoding="utf-8") as f:
        config = yaml.safe_load(f)
    return config


load_config()
