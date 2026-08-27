from . import views
from django.urls import path
urlpatterns = [
    path('jobs/',views.jobs,name='jobs'),
]