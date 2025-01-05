from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os

load_dotenv()

class Config(BaseSettings):
    SECRET_KEY: str = os.getenv("OPENAI_API_KEY")
    OPENAI_API_KEY: str = os.getenv("SECRET_KEY")
    
config = Config()
