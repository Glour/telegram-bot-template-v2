from functools import lru_cache

from pydantic import Field
from pydantic_settings import SettingsConfigDict, BaseSettings

from settings.bot_settings import BotSettings
from settings.db_settings import DatabaseSettings, RedisSettings
from settings.logging_settings import LoggingSettings


class AppSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=str('.env'),
        env_file_encoding="utf-8",
        env_nested_delimiter="__",
        extra="ignore",
    )

    is_development: bool = Field(default=False)

    postgres: DatabaseSettings
    logging: LoggingSettings
    bot: BotSettings
    redis: RedisSettings


@lru_cache(maxsize=1)
def get_app_settings() -> AppSettings:
    return AppSettings()
