from . import views
from django.urls import path

urlpatterns = [
    path('notifications/',views.notifications,name='notifications'),
]