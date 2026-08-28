from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('companies', views.CompanyViewSet,basename='companies')
router.register('employees', views.CompanyEmployeeViewSet,basename='employees')
urlpatterns=router.urls
