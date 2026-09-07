from multiprocessing.resource_tracker import register

from . import views
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('applications', views.ApplicationViewSet,basename='applications')
urlpatterns = router.urls