from . import views
from django.urls import path
urlpatterns = [
    path('skills/',views.skills,name='skills'),
]