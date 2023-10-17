import aiohttp
import faust

from services.delivery import EmailService
from services.notifications import NotificationsService
from core.config import CONFIG
from core.enums import KafkaTopics
from models.records import LikeComment, NewUser, Notification

app = faust.App(CONFIG.faust.title, broker=CONFIG.kafka.url)

TOPICS = {
    'notifications': app.topic(KafkaTopics.notifications.name, value_type=Notification),
    'new_users': app.topic(KafkaTopics.new_users.name, value_type=NewUser),
    'comment_likes': app.topic(KafkaTopics.comment_likes.name, value_type=LikeComment),
}


@app.agent(TOPICS['notifications'])
async def mailing_list(notifications: faust.StreamT[Notification]):
    """Kafka consumer function that reads messages from the 'notifications' topic.

    Args:
        notifications: Notifications publications
    """
    async with aiohttp.ClientSession() as session:
        async for notification in notifications:
            service = NotificationsService(session)
            offset, limit = 0, 50
            while True:
                response = await service.get_notification_users(
                    notification_id=notification.notification_id,
                    offset=offset if offset == 0 else offset + limit,
                    limit=limit,
                )
                if not response or not (users := response['results']):
                    break
                for user in users:
                    if user['delivery_method'] == 'email':
                        result = EmailService.send(user, notification)
                        await service.set_delivery_status(user['user_notification'], was_sent=result)
                offset += limit


@app.agent(TOPICS['new_users'])
async def welcome_letter(new_users: faust.StreamT[NewUser]):
    """Kafka consumer function that reads messages from the 'new_users' topic.

    Args:
        new_users: New users publications
    """
    async with aiohttp.ClientSession() as session:
        async for new_user in new_users:
            service = NotificationsService(session)
            title = 'Welcome Email'
            text = 'Thank you for registering on our website!'
            if response := await service.create_user_notification(new_user.email, title, text):
                result = EmailService.send(new_user.email, title, text)
                await service.set_delivery_status(user_notification_id=response['id'], was_sent=result)


@app.agent(TOPICS['comment_likes'])
async def alert_like(comment_likes: faust.StreamT[LikeComment]):
    """Kafka consumer function that reads messages from the 'comment_likes' topic.

    Args:
        comment_likes: Comment likes publications
    """
    async for comment_like in comment_likes:
        ...


if __name__ == '__main__':
    app.main()
