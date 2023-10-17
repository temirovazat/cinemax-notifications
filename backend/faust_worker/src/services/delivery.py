from abc import ABC, abstractmethod
from typing import Dict

from models.records import Notification


class DeliveryService(ABC):
    """Abstract service for delivering notifications."""

    @classmethod
    @abstractmethod
    def send(cls, user: Dict, notification: Notification) -> bool:
        """Send a notification.

        Args:
            user: User data
            notification: Notification

        Returns:
            bool: True if the message is sent, else False
        """


class EmailService(DeliveryService):
    """Service for delivering notifications via email."""

    @classmethod
    def send(cls, user: Dict, notification: Notification) -> bool:
        """Send a notification via EMAIL.

        Args:
            user: User data
            notification: Notification

        Returns:
            bool: True if the message is sent, else False
        """
        return True


class SmsService(DeliveryService):
    """Service for delivering notifications via phone number."""

    @classmethod
    def send(cls, user: Dict, notification: Notification) -> bool:
        """Send a notification via SMS.

        Args:
            user: User data
            notification: Notification

        Returns:
            bool: True if the message is sent, else False
        """
        return True


class PushService(DeliveryService):
    """Service for delivering notifications using Push technology."""

    @classmethod
    def send(cls, user: Dict, notification: Notification) -> bool:
        """Send a notification via Push.

        Args:
            user: User data
            notification: Notification

        Returns:
            bool: True if the message is sent, else False
        """
        return True
