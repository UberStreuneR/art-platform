from pydantic import BaseSettings, PostgresDsn
from os import getenv

class Settings(BaseSettings):
    database_url: PostgresDsn


def get_settings() -> Settings:
    settings = Settings()
    
    # POSTGRES_DB = test_db, for test purposes
    if (db := getenv("POSTGRES_DB")) is not None:
        settings.database_url = PostgresDsn.build(
            scheme=settings.database_url.scheme,
            user=settings.database_url.user,
            password=settings.database_url.password,
            host=settings.database_url.host,
            port=settings.database_url.port,
            path = f'/{db}'
        )
    return settings