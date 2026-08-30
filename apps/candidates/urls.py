from . import views
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register("candidates", views.CandidateViewSet,basename="candidate")
urlpatterns = router.urls