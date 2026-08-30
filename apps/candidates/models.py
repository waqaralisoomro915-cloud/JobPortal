from django.db import models
from ..accounts.models import User
class Candidate(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='candidate')
    headline = models.CharField(max_length=200,blank=True)
    bio = models.TextField(blank=True)
    phone = models.CharField(max_length=20,blank=True)
    location = models.CharField(max_length=150,blank=True)
    profile_picture = models.ImageField(upload_to='candidates/profile_pics',blank=True,null=True)
    resume = models.FileField(upload_to='candidates/resume',blank=True,null=True)
    linkedin_url = models.URLField(blank=True)
    github_url = models.URLField(blank=True)
    portfolio_url = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.user.get_full_name() or self.user.email