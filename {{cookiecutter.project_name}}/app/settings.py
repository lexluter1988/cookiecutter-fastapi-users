import functools

from pydantic.v1 import BaseSettings


class Settings(BaseSettings):
    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'
        env_prefix = ''

    app_version: str = '0.0.1'
    jwt_lifetime_seconds: int = 3600
    jwt_secret: str = 'SECRET'
    database_url: str = 'sqlite+aiosqlite:///./test_app.db'
    debug: bool = False
    log_level: str = 'DEBUG'


@functools.lru_cache
def get_settings() -> Settings:
    return Settings()
