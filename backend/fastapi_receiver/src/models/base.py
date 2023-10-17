from abc import ABC, abstractmethod
from typing import Callable

import orjson
from pydantic import BaseModel


def orjson_dumps(data: object, *, default: Callable) -> str:
    """Decode data into Unicode for parsing objects based on the Pydantic class.

    Args:
        data: Data to convert
        default: Function for objects that cannot be serialized.

    Returns:
        str: JSON string
    """
    return orjson.dumps(data, default=default).decode()


class OrjsonMixin(BaseModel):
    """Mixin for replacing standard JSON handling with a faster one."""

    class Config:
        """Serialization settings."""

        json_loads = orjson.loads
        json_dumps = orjson_dumps


class KafkaEvent(ABC, OrjsonMixin):
    """Abstract model of an event (message) received in the Kafka message broker."""

    @property
    @abstractmethod
    def key(self) -> str:
        """Property with the event key for partitioning data.

        Returns:
            str: Partition key
        """

    @property
    def value(self) -> str:
        """Property with the event's value, which is the message content.

        Returns:
            str: Event content
        """
        return self.json()
