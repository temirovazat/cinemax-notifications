import logging
from http import HTTPStatus
from typing import Dict, Optional

import aiohttp

from core.config import CONFIG
from core.decorators import aiohttp_error_handler


class NotificationsService:
    """Service for making API requests to the notifications microservice in the admin panel."""

    def __init__(self, session: aiohttp.ClientSession):
        """Initialize with an HTTP session between the server and client.

        Args:
            session: Object for asynchronous HTTP operations
        """
        self.session = session

    @aiohttp_error_handler
    async def get_notification_users(self, notification_id: str, offset: int, limit: int) -> Optional[Dict]:
        """Retrieve users for a specific notification.

        Args:
            notification_id: Notification identifier
            offset: Offset
            limit: Limit

        Returns:
            Optional[Dict]: JSON response
        """
        async with self.session.get(
            url='http://{service_url}/{api_endpoint}/'.format(
                service_url=CONFIG.admin.url,
                api_endpoint=f'api/v1/notifications/{notification_id}/users',
            ),
            params={'offset': offset, 'limit': limit},
        ) as response:
            if response.status == HTTPStatus.OK:
                return (await response.json())
            else:
                logging.error(f'HTTP error - {response.status}, {response}')
                return None

    @aiohttp_error_handler
    async def create_user_notification(self, email: str, title: str, text: str) -> Optional[Dict]:
        """Create a user and associate a notification with them.

        Args:
            email: Email address
            title: Notification title
            text: Notification text

        Returns:
            Optional[Dict]: JSON response
        """
        async with self.session.post(
            url='http://{service_url}/{api_endpoint}/'.format(
                service_url=CONFIG.admin.url,
                api_endpoint='api/v1/users_notifications',
            ),
            json={'email': email, 'title': title, 'text': text},
        ) as response:
            if response.status == HTTPStatus.CREATED:
                return (await response.json())
            else:
                logging.error(f'HTTP error - {response.status}, {response}')
                return None

    @aiohttp_error_handler
    async def set_delivery_status(self, user_notification_id: str, was_sent: bool) -> Optional[Dict]:
        """Set the flag indicating whether the notification was sent or not.

        Args:
            user_notification_id: User notification identifier
            was_sent: Whether the notification was sent

        Returns:
            dict | None: JSON response
        """
        async with self.session.patch(
            url='http://{service_url}/{api_endpoint}/'.format(
                service_url=CONFIG.admin.url,
                api_endpoint=f'api/v1/users_notifications/{user_notification_id}',
            ),
            json={'was_sent': was_sent},
        ) as response:
            if response.status == HTTPStatus.OK:
                return (await response.json())
            else:
                logging.error(f'HTTP error - {response.status}, {response}')
                return None
