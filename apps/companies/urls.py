from . import views
from django.urls import path

urlpatterns = [
    path('companies/',views.companies,name='companies'),
]