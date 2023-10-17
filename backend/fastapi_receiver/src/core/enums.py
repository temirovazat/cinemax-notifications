from enum import Enum


class KafkaTopics(Enum):
    """Class with an enumeration of Kafka topics."""

    video_progress = 'video_progress'
    new_users = 'new_users'
    comment_likes = 'comment_likes'
    notifications = 'notifications'
