from django.contrib import admin

from notifications.models import UserNotification


class UserNotificationInline(admin.TabularInline):
    """Class for including users in the notification admin panel."""

    model = UserNotification
    autocomplete_fields = ('user',)
    readonly_fields = ('was_sent',)
