from typing import List

from django.contrib import admin
from django.core.handlers.wsgi import WSGIRequest
from django.utils.translation import gettext_lazy as _

from notifications.base.admin import UserNotificationInline
from notifications.forms import NotificationForm
from notifications.models import Notification, User, UserNotification
from notifications.utils import publish_notification


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Admin class for users with notification settings."""

    list_display = ('id', 'email', 'delivery_method')
    list_filter = ('delivery_method',)
    search_fields = ('email',)


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    """Admin class for notifications."""

    form = NotificationForm
    inlines = (UserNotificationInline,)
    list_display = ('id', 'title', 'text')
    list_filter = ('title',)
    search_fields = ('id',)

    def save_related(self, request: WSGIRequest, form: NotificationForm, formsets: List, change: bool):
        """Override data save to publish a notification creation event.

        Args:
            request: HTTP request,
            form: Model form
            formsets: List of inline forms
            change: Boolean value based on whether an object is added or modified
        """
        super().save_related(request, form, formsets, change)
        notification: Notification = form.instance
        if form.cleaned_data.get('all_users'):
            notification.users.add(*User.objects.all())
        publish_notification(notification)


@admin.register(UserNotification)
class UserNotificationAdmin(admin.ModelAdmin):
    """Admin class for user notification sending history."""

    list_display = ('id', 'notification', 'get_user_email', 'was_sent')
    list_filter = ('was_sent',)
    search_fields = ('id',)

    @admin.display(description=_('email'))
    def get_user_email(self, obj: UserNotification) -> str:
        """Display user email.

        Args:
            obj: User notification object

        Returns:
            str: Email
        """
        return obj.user.email
