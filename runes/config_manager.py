import json
from langchain.llms import OpenAI

class ConfigManager:
    def __init__(self, config_path):
        self.config_path = config_path
        self.llm = OpenAI()

    def update_config(self, symbol, template):
        config = self.load_config()
        config[symbol] = template
        self.save_config(config)

    def generate_ai_mapping(self, description):
        response = self.llm.generate(description)
        mappings = response.split('\n')
        for mapping in mappings:
            symbol, template = mapping.split('=', 1)
            self.update_config(symbol.strip(), template.strip())

    def load_config(self):
        with open(self.config_path, 'r') as file:
            return json.load(file)

    def save_config(self, config):
        with open(self.config_path, 'w') as file:
            json.dump(config, file, indent=4)
