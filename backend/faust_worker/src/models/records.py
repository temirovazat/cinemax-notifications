import faust


class Notification(faust.Record):
    """Model for publishing notifications."""

    notification_id: str
    title: str
    text: str


class NewUser(faust.Record):
    """Model for publishing new users."""

    user_id: str
    email: str


class LikeComment(faust.Record):
    """Model for publishing comment likes."""

    user_id: str
    comment_id: str
