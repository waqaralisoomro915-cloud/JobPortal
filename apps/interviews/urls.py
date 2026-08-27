from . import views
from django.urls import path
urlpatterns = [
    path('interviews/',views.interviews,name='interviews'),
]