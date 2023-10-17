from django import forms

from notifications.models import Notification


class NotificationForm(forms.ModelForm):
    """Form for the notification model with an additional field.

    Attributes:
        all_users (forms.BooleanField): A field to send notifications to all users.
    """

    all_users = forms.BooleanField(
        required=False,
        label='All Users',
        help_text='Send the notification to all users',
    )

    class Meta:
        """Metadata."""

        model = Notification
        fields = '__all__'
