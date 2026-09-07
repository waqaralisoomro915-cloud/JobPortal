from . import views
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('notifications',views.NotificationViewSet,basename='notifications')
urlpatterns = router.urls