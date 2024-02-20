from runes import RunesEngine, ConfigManager

# Assume config.json already exists and contains mappings
config_path = "examples/config.json"

# Initialize the engine and config manager
engine = RunesEngine(config_path)
config_manager = ConfigManager(config_path)

# Example pseudo-code
pseudo_code = "🚀 PlayerSpawn\n➡️ ✨ SetHealth (🔢 Health=100)"

# Translate pseudo-code to actual code
print(engine.translate_pseudo_code(pseudo_code))
