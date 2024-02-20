class SystemPromptGenerator:
    def __init__(self, config):
        self.config = config

    def generate_prompt(self):
        prompts = []
        for symbol, template in self.config.items():
            prompts.append(f"// {symbol} maps to {template}")
        return '\n'.join(prompts)
