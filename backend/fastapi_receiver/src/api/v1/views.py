from http import HTTPStatus

from fastapi import Body, Depends, HTTPException, Response

from services.post_event import PostEventService, get_post_event_service
from core.enums import KafkaTopics
from models import events


async def publish_new_user(
    new_user: events.NewUser = Body(title='New User Event'),
    kafka: PostEventService = Depends(get_post_event_service),
) -> Response:
    """Publish a new user event.

    Args:
        new_user: The 'new user' event
        kafka: Object for publishing the event to Kafka

    Raises:
        HTTPException: 400 error if the Kafka server is unavailable

    Returns:
        Response: HTTP response with a 200 status code
    """
    ok = await kafka.produce(topic=KafkaTopics.new_users, event=new_user)
    if not ok:
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST)
    return Response(status_code=HTTPStatus.CREATED)


async def publish_like_comment(
    like_comment: events.LikeComment = Body(title='Like Comment Event'),
    kafka: PostEventService = Depends(get_post_event_service),
) -> Response:
    """Publish a like comment event.

    Args:
        like_comment: The 'like comment' event
        kafka: Object for publishing the event to Kafka

    Raises:
        HTTPException: 400 error if the Kafka server is unavailable

    Returns:
        Response: HTTP response with a 200 status code
    """
    ok = await kafka.produce(topic=KafkaTopics.comment_likes, event=like_comment)
    if not ok:
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST)
    return Response(status_code=HTTPStatus.CREATED)


async def publish_notification(
    notification: events.Notification = Body(title='User Notification Event'),
    kafka: PostEventService = Depends(get_post_event_service),
) -> Response:
    """Publish a user notification event.

    Args:
        notification: The 'user notification' event
        kafka: Object for publishing the event to Kafka

    Raises:
        HTTPException: 400 error if the Kafka server is unavailable

    Returns:
        Response: HTTP response with a 200 status code
    """
    ok = await kafka.produce(topic=KafkaTopics.notifications, event=notification)
    if not ok:
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST)
    return Response(status_code=HTTPStatus.CREATED)
