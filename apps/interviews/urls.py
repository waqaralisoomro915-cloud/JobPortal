from . import views
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('interviews',views.InterviewViewSet,basename='interviews')
urlpatterns = router.urls