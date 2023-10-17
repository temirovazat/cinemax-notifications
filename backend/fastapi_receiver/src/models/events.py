from datetime import datetime
from uuid import UUID

from pydantic import EmailStr

from models.base import KafkaEvent


class NewUser(KafkaEvent):
    """Model for publishing a new user event."""

    user_id: UUID
    email: EmailStr

    @property
    def key(self) -> str:
        """Property for the event key for partitioning by date.

        Returns:
            str: Partitioning key
        """
        return datetime.now().strftime('%m/%d/%Y, %H:%M:%S')


class LikeComment(KafkaEvent):
    """Model for publishing a like to a user's comment event."""

    user_id: UUID
    comment_id: UUID

    @property
    def key(self) -> str:
        """Property for the event key for partitioning by users and comments.

        Returns:
            str: Partitioning key
        """
        return '{user}::{comment}'.format(user=self.user_id, comment=self.comment_id)


class Notification(KafkaEvent):
    """Model for publishing user notifications."""

    notification_id: UUID
    title: str
    text: str

    @property
    def key(self) -> str:
        """Property for the event key for partitioning by date.

        Returns:
            str: Partitioning key
        """
        return datetime.now().strftime('%m/%d/%Y, %H:%M:%S')
