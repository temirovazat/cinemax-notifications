import logging

import requests
from django.conf import settings
from requests.exceptions import ConnectionError, HTTPError

from notifications.models import Notification


def publish_notification(obj: Notification):
    """Publish an event to Kafka via a request to an external microservice.

    Args:
        obj: Notification object
    """
    try:
        requests.post(
            url='http://{service_url}/api/events/v1/notification'.format(service_url=settings.EVENT_SOURCING_URL),
            json={'notification_id': str(obj.id), 'title': obj.title, 'text': obj.text},
        ).raise_for_status()
    except HTTPError as exc:
        logging.error(f'Failed to publish the event due to {exc}')
    except ConnectionError as exc:
        logging.critical(f'Connection error: {exc}')
    else:
        logging.info('Notification created and sent for processing!')
