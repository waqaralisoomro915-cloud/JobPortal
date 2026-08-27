from .import views
from django.urls import path

urlpatterns =[
    path('common/',views.common,name='common'),
]