from django.db.models import F, QuerySet
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.pagination import LimitOffsetPagination

from api.v1.serializers import UserSerializer, UserNotificationSerializer, UserNotificationCreateSerializer
from notifications.models import Notification, User, UserNotification
from notifications.base.enums import DeliveryMethod


class UserNotificationCreate(generics.CreateAPIView):
    """High-level view class for creating a user notification."""

    queryset = UserNotification.objects.all()
    serializer_class = UserNotificationCreateSerializer


class UserNotificationUpdate(generics.UpdateAPIView):
    """High-level view class for updating a user notification."""

    queryset = UserNotification.objects.all()
    serializer_class = UserNotificationSerializer


class UsersListByNotification(generics.ListAPIView):
    """High-level view class for getting a list of users by notification."""

    serializer_class = UserSerializer
    pagination_class = LimitOffsetPagination

    def get_queryset(self) -> QuerySet[User]:
        """Prepare a query with users for the notification, excluding those who have disabled notifications.

        Returns:
            QuerySet[User]: Users in the notification
        """
        notification = get_object_or_404(Notification, id=self.kwargs['pk'])
        return notification.users.exclude(delivery_method=DeliveryMethod.NONE).annotate(
            user_notification=F('usernotification'),
        )
