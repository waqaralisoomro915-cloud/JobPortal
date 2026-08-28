from django.db import models
from ..accounts.models import User

class Company(models.Model):
    COMPANY_SIZE_CHOICES=[
        ("1-10","1-10 Employees"),
        ("11-50","11-50 Employees"),
        ("51-100","51-100 Employees"),
        ("101-200","101-200 Employees"),
        ("201-300","201-300 Employees"),
        ("301-400","301-400 Employees"),
        ("401-500","401-500 Employees"),
        ("501-600","501-600 Employees"),
        ("601-700","601-700 Employees"),
        ("701-800","701-800 Employees"),
        ("801-1000","801-1000 Employees"),
        ("1001-2000","1001-2000 Employees"),
    ]
    company_name=models.CharField(max_length=200)
    description=models.TextField(blank=True)
    logo=models.ImageField(upload_to='companies/',blank=True,null=True)
    website=models.URLField(blank=True)
    industry=models.CharField(max_length=100,blank=True)
    company_size=models.CharField(max_length=20,choices=COMPANY_SIZE_CHOICES, blank=True)
    location=models.CharField(max_length=100,blank=True)
    founded_year=models.PositiveIntegerField(blank=True,null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.company_name

class CompanyEmployee(models.Model):
    company=models.ForeignKey(Company,on_delete=models.CASCADE,related_name='employees')
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='company_memberships')
    class Role(models.TextChoices):
        OWNER = "OWNER", "Owner"
        RECRUITER = "RECRUITER", "Recruiter"
        HR = "HR", "HR"
    role=models.CharField(choices=Role.choices,max_length=40)
    joined_at=models.DateTimeField(auto_now_add=True)
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['company','user'],
                name='unique_company_employee',
            )
        ]
    def __str__(self):
        return f"{self.user}- {self.company}"
