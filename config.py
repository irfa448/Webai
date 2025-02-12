import os
import json
from pathlib import Path

def load_config():
    # Default config
    config = {
        "GOOGLE_API_KEY": None
    }
    
    # Try to load from config.json if exists
    config_file = Path("config.json")
    if config_file.exists():
        try:
            with open(config_file) as f:
                config.update(json.load(f))
        except Exception as e:
            print(f"Error loading config.json: {e}")
    
    # Environment variables take precedence
    if os.environ.get("GOOGLE_API_KEY"):
        config["GOOGLE_API_KEY"] = os.environ.get("GOOGLE_API_KEY")
        
    return config

def get_api_key():
    config = load_config()
    api_key = config.get("GOOGLE_API_KEY")
    
    if not api_key:
        raise ValueError(
            "GOOGLE_API_KEY tidak ditemukan! "
            "Pastikan kamu sudah mengatur API key di environment variable "
            "atau di file config.json"
        )
    
    return api_key
