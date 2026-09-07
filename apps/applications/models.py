from django.db import models
from ..candidates.models import Candidate
from ..jobs.models import Job


# Create your models here.
class Application(models.Model):
    class Status(models.TextChoices):
        Applied="APPLIED", "Applied"
        REVIEWING="REVIEWING", "Reviewing"
        SHORTLISTED="SHORTLISTED", "Short Listed"
        REJECTED="REJECTED", "Rejected"
        HIRED="HIRED", "Hired"
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE,related_name='applications')
    job = models.ForeignKey(Job, on_delete=models.CASCADE,related_name='applications')
    cover_letter = models.CharField(max_length=100,default='')
    resume = models.FileField(upload_to='applicantResume/',null=True,blank=True)
    status = models.CharField(choices=Status.choices, default=Status.Applied,max_length=20)
    applied_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['candidate', 'job'],
                name='unique_application',
            )
        ]
    def __str__(self):
        return f'{self.candidate.user.email} - {self.job.title}'