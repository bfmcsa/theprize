from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, CompanyViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'companies', CompanyViewSet, basename='company')

urlpatterns = router.urls