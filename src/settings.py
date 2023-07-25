from functools import lru_cache
from typing import Annotated

from fastapi.params import Depends
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    fastapi_host: str
    fastapi_port: int
    fastapi_debug: bool
    fastapi_reload: bool
    fastapi_workers: int

    db_host: str
    db_port: int
    db_name: str
    db_user: str
    db_password: str

    @property
    def db_dsn(self):
        return f"postgresql+asyncpg://{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}"

    class Config:
        env_file = ".env.template"


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    return Settings()


AppSettings = Annotated[Settings, Depends(get_settings)]
