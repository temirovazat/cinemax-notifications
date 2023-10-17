import logging
from functools import lru_cache

from aiokafka import AIOKafkaProducer
from aiokafka.errors import KafkaError
from fastapi import Depends

from core.enums import KafkaTopics
from db.kafka import get_kafka
from models.base import KafkaEvent


class PostEventService:
    """Service for sending events to the Kafka message broker."""

    def __init__(self, kafka: AIOKafkaProducer):
        """Initialize the class by accepting a Kafka producer client.

        Args:
            kafka: Kafka producer
        """
        self.kafka = kafka

    async def produce(self, topic: KafkaTopics, event: KafkaEvent) -> bool:
        """Publish an event to the Kafka stream.

        Args:
            topic: Kafka topic
            event: Event to publish

        Returns:
            bool: True if the message is sent; False otherwise
        """
        try:
            result = await self.kafka.send_and_wait(topic.name, event.value, event.key)
        except KafkaError as exc:
            logging.error(exc)
            return False
        logging.info(result)
        return True


@lru_cache()
def get_post_event_service(kafka: AIOKafkaProducer = Depends(get_kafka)) -> PostEventService:
    """Create a PostEventService object as a singleton.

    Args:
        kafka: Kafka connection

    Returns:
        PostEventService: Service for sending events to Kafka
    """
    return PostEventService(kafka)
