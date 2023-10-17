from functools import lru_cache

from pydantic import BaseModel, BaseSettings, Field


class KafkaConfig(BaseModel):
    """Class with Kafka connection settings."""

    host: str = 'localhost'
    port: int = 29092

    @property
    def url(self) -> str:
        """Property with the broker's URL.

        Returns:
            str: Kafka URL
        """
        return 'kafka://{host}:{port}'.format(host=self.host, port=self.port)


class FaustConfig(BaseModel):
    """Class with Faust connection settings."""

    title: str = 'Worker'


class AdminConfig(BaseModel):
    """Class with admin panel connection settings."""

    url: str = 'localhost:8000'


class MainSettings(BaseSettings):
    """The main class with all settings."""

    faust: FaustConfig = Field(default_factory=FaustConfig)
    kafka: KafkaConfig = Field(default_factory=KafkaConfig)
    admin: AdminConfig = Field(default_factory=AdminConfig)


@lru_cache()
def get_settings() -> MainSettings:
    """
    Create a settings object in a singleton instance.

    Returns:
        MainSettings: Object with settings
    """
    return MainSettings(_env_file='.env', _env_nested_delimiter='_')  # type: ignore[call-arg]


CONFIG = get_settings()
