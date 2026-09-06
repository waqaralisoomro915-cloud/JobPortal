from rest_framework.routers import DefaultRouter
from . import views
router = DefaultRouter()
router.register('skills', views.SkillViewSet,basename='skills')
urlpatterns = router.urls