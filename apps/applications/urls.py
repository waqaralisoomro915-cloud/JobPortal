from . import views
from django.urls import path
urlpatterns = [
    path('applications/',views.applications,name='applications'),
]