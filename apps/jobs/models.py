from django.db import models
from ..companies.models import Company
class Job(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE,related_name='jobs')
    class WorkMode(models.TextChoices):
        REMOTE = "REMOTE", "Remote"
        HYBRID = "HYBRID", "Hybrid"
        ON_SITE = "ON_SITE", "On Site"

    class JobType(models.TextChoices):
        FULL_TIME = "FULL_TIME", "Full Time"
        PART_TIME = "PART_TIME", "Part Time"
        CONTRACT = "CONTRACT", "Contract"
        INTERNSHIP = "INTERNSHIP", "Internship"
        FREELANCE = "FREELANCE", "Freelance"

    title = models.CharField(max_length=100,blank=False)
    description = models.TextField(max_length=100,blank=True,null=True)
    requirements = models.TextField(max_length=100,blank=True,null=True)
    job_type = models.CharField(max_length=20,choices=JobType.choices)
    experience_years = models.PositiveIntegerField(null=True,blank=True)
    location = models.CharField(max_length=100)
    work_mode = models.CharField(max_length=20,choices=WorkMode.choices)
    city = models.CharField(max_length=100)
    salary_min = models.PositiveIntegerField(null=True,blank=True)
    salary_max = models.PositiveIntegerField(null=True,blank=True)
    deadline = models.DateField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title