from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache

class Settings(BaseSettings):
    PROJECT_NAME: str = "FastAPI AI Project"
    API_V1_STR: str = "/api/v1"
    
    # Add other settings here (e.g., database URL, API keys)
    # GOOGLE_API_KEY: str

    model_config = SettingsConfigDict(env_file=".env")

@lru_cache
def get_settings():
    return Settings()
