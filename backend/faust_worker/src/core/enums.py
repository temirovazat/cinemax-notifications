from enum import Enum


class KafkaTopics(Enum):
    """Class with a list of Kafka topics."""

    new_users = 'new_users'
    comment_likes = 'comment_likes'
    notifications = 'notifications'
