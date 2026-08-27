from . import views
from django.urls import path

urlpatterns = [
    path('candidates/',views.candidates,name='candidates'),
]