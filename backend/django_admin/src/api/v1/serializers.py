from typing import Dict

from rest_framework import serializers

from notifications.models import Notification, User, UserNotification


class UserSerializer(serializers.ModelSerializer):
    """Serializer for the user model."""

    user_notification = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        """Metadata."""

        fields = ('id', 'email', 'delivery_method', 'user_notification')
        model = User


class UserNotificationSerializer(serializers.ModelSerializer):
    """Serializer for the user notification model."""

    class Meta:
        """Metadata."""

        fields = ('id', 'notification', 'user', 'was_sent')
        model = UserNotification


class UserNotificationCreateSerializer(serializers.ModelSerializer):
    """Serializer for creating user notifications."""

    email = serializers.CharField(write_only=True)
    title = serializers.CharField(write_only=True)
    text = serializers.CharField(write_only=True)

    class Meta:
        """Metadata."""

        fields = ('id', 'email', 'title', 'text')
        model = UserNotification

    def create(self, validated_data: Dict) -> UserNotification:
        """Override data creation to create notification and user objects.

        Args:
            validated_data: Data after validation.

        Returns:
            UserNotification: User notification.
        """
        email = validated_data.pop('email')
        data = {
            'notification': Notification.objects.create(**validated_data),
            'user': User.objects.create(email=email),
        }
        return super().create(data)
