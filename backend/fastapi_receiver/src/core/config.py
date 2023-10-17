from functools import lru_cache

from pydantic import BaseModel, BaseSettings, Field


class KafkaConfig(BaseModel):
    """Class with Kafka connection settings."""

    host: str = 'localhost'
    port: int = 29092


class FastApiConfig(BaseModel):
    """Class with FastAPI connection settings."""

    host: str = '0.0.0.0'
    port: int = 8000
    debug: bool = False
    secret_key: str = 'secret_key'
    title: str = 'Post-only API for publishing events'


class MainSettings(BaseSettings):
    """Class with the main project settings."""

    fastapi: FastApiConfig = Field(default_factory=FastApiConfig)
    kafka: KafkaConfig = Field(default_factory=KafkaConfig)


@lru_cache()
def get_settings():
    """Create a settings object as a singleton.

    Returns:
        MainSettings: Object with settings
    """
    return MainSettings(_env_file='.env', _env_nested_delimiter='_')


CONFIG = get_settings()
