from openai import OpenAI
import yaml
from pathlib import Path


def load_config():
    config_path = Path(__file__).resolve().parents[2] / "config" / "config.yaml"
    with config_path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f)


class DeepSeekAPI:
    def __init__(self):
        config = load_config()
        api_key = config["deepseek"]["api_key"]
        self.client = OpenAI(api_key=api_key, base_url="https://api.deepseek.com/v1")

    def chat(self, prompt, model="deepseek-chat"):
        response = self.client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=600,
        )
        return response.choices[0].message.content.strip()
