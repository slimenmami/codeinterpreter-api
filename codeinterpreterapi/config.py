from typing import Optional
import streamlit as st

from dotenv import load_dotenv
from pydantic_settings import BaseSettings

# .env file
load_dotenv(dotenv_path="./.env")


class CodeInterpreterAPISettings(BaseSettings):
    """
    CodeInterpreter API Config
    """

    VERBOSE: bool = False

    OPENAI_API_KEY: Optional[str] = st.secrets["open_ai_key"]

    CODEBOX_API_KEY: Optional[str] = None

    HISTORY_BACKEND: Optional[str] = None
    REDIS_URL: str = "redis://localhost:6379"
    POSTGRES_URL: str = "postgresql://postgres:postgres@localhost:5432/postgres"


settings = CodeInterpreterAPISettings()
