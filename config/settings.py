from pydantic_settings import BaseSettings

from dotenv import load_dotenv


load_dotenv()


class Settings(BaseSettings):
    version_repr: str = "1.0 ❤️"
    bot_token: str
    owner_id: int


settings = Settings()
