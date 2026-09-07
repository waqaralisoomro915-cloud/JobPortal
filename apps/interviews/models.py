from django.db import models

from ..applications.models import Application
from ..accounts.models import User


class Interview(models.Model):

    class InterviewType(models.TextChoices):
        ONLINE = "ONLINE", "Online"
        PHONE = "PHONE", "Phone"
        IN_PERSON = "IN_PERSON", "In Person"

    class Status(models.TextChoices):
        SCHEDULED = "SCHEDULED", "Scheduled"
        COMPLETED = "COMPLETED", "Completed"
        CANCELLED = "CANCELLED", "Cancelled"
        RESCHEDULED = "RESCHEDULED", "Rescheduled"
        
    application = models.ForeignKey(Application,on_delete=models.CASCADE, related_name="interviews")
    interviewer = models.ForeignKey( User, on_delete=models.SET_NULL,null=True,   related_name="conducted_interviews" )
    scheduled_at = models.DateTimeField()
    duration = models.PositiveIntegerField(help_text="Duration in minutes" )
    interview_type = models.CharField( max_length=20, choices=InterviewType.choices)
    meeting_link = models.URLField(blank=True, null=True )
    status = models.CharField(max_length=20,choices=Status.choices,default=Status.SCHEDULED)
    notes = models.TextField(blank=True)
    feedback = models.TextField( blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True )
    def __str__(self):
        return f"Interview - {self.application}"