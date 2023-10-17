from uuid import uuid4

from celery import shared_task

from notifications.models import Notification, User
from notifications.utils import publish_notification


@shared_task
def get_new_films(title: str, text: str) -> bool:
    """Generate notifications for new movies.

    Args:
        title: Title
        text: Text

    Returns:
        bool: Whether the task was executed successfully
    """
    fake_new_films_from_movies = [{'id': uuid4()} for _ in range(6)]
    notification = Notification.objects.create(
        title=title,
        text=text + '\n' + f'New movies: {fake_new_films_from_movies}',
    )
    notification.users.add(*User.objects.all())
    publish_notification(notification)
    return True


@shared_task
def bookmark_reminder(title: str, text: str):
    """Generate notifications for users who haven't visited their bookmarks in a while.

    Args:
        title: Title
        text: Text

    Returns:
        bool: Whether the task was executed successfully
    """
    fake_users_from_ugc = [{'id': uuid4()} for _ in range(10)]
    users = User.objects.filter(id__in=[user['id'] for user in fake_users_from_ugc])
    if not users:
        return False
    notification = Notification.objects.create(title=title, text=text)
    notification.users.add(*users)
    publish_notification(notification)
    return True
