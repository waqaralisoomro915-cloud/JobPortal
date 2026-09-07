from django.db import models

from ..accounts.models import User


class Notification(models.Model):

    class NotificationType(models.TextChoices):
        APPLICATION_SUBMITTED = (
            "APPLICATION_SUBMITTED",
            "Application Submitted",
        )
        APPLICATION_STATUS_CHANGED = (
            "APPLICATION_STATUS_CHANGED",
            "Application Status Changed",
        )
        INTERVIEW_SCHEDULED = (
            "INTERVIEW_SCHEDULED",
            "Interview Scheduled",
        )
        INTERVIEW_RESCHEDULED = (
            "INTERVIEW_RESCHEDULED",
            "Interview Rescheduled",
        )
        INTERVIEW_CANCELLED = (
            "INTERVIEW_CANCELLED",
            "Interview Cancelled",
        )

    recipient = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="notifications",
    )

    notification_type = models.CharField(
        max_length=50,
        choices=NotificationType.choices,
    )

    title = models.CharField(
        max_length=255,
    )

    message = models.TextField()

    is_read = models.BooleanField(
        default=False,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    read_at = models.DateTimeField(
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"{self.recipient} - {self.title}"