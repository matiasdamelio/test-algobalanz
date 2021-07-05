from pydantic import BaseSettings
import os


class Settings(BaseSettings):

    PROJECT_NAME: str = "ALGOBALANZ CHALLENGE"
    API_V1_STR: str = "/api/v1"

    data: list = []
    market_data: dict = {}
    iterator: int = 0

    manager: object = None


settings = Settings()
