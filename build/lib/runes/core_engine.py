import json

class RunesEngine:
    def __init__(self, config_path):
        self.config = self.load_config(config_path)

    def load_config(self, config_path):
        with open(config_path, 'r') as file:
            return json.load(file)

    def translate_pseudo_code(self, pseudo_code):
        translated_code = ""
        for line in pseudo_code.split('\n'):
            symbol, action = line.strip().split(' ', 1)
            if symbol in self.config:
                translated_code += self.config[symbol].format(action) + '\n'
            else:
                translated_code += f"// Unmapped symbol: {symbol}" + '\n'
        return translated_code
