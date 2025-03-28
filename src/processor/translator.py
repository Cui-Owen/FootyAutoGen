from pathlib import Path
from .deepseek_api import DeepSeekAPI


class Translator:
    def __init__(self):
        self.api = DeepSeekAPI()
        prompt_path = (
            Path(__file__).resolve().parents[2]
            / "config"
            / "prompts"
            / "summary_prompt.txt"
        )
        with open(prompt_path, "r", encoding="utf-8") as f:
            self.prompt_template = f.read()

    def translate_and_summarize(self, english_text):
        prompt = self.prompt_template.format(news_content=english_text)
        chinese_summary = self.api.chat(prompt)
        return chinese_summary
