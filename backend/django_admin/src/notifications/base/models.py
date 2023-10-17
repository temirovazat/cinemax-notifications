import uuid

from django.db import models


class UUIDMixin(models.Model):
    """An abstract model for generating primary keys."""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        """Metadata."""

        abstract = True


class TimeStampedMixin(models.Model):
    """An abstract model for timestamping."""

    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        """Metadata."""

        abstract = True
