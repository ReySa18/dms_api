from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "AI DMS Backend"
    DATABASE_URL: str
    JWT_SECRET: str
    RAG_SERVICE_URL: str

    class Config:
        env_file = ".env"

settings = Settings()

