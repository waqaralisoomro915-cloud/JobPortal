from . import views
from django.urls import path
urlpatterns = [
    path('accounts/',views.accounts,name='accounts'),

]