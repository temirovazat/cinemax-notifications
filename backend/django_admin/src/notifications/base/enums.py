from django.db import models
from django.utils.translation import gettext_lazy as _


class DeliveryMethod(models.TextChoices):
    """Auxiliary model for selecting the notification delivery method."""

    EMAIL = 'email', _('email')
    SMS = 'sms', _('sms')
    PUSH = 'push', _('push')
    NONE = 'none', _('none')
