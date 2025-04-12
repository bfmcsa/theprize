from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import CampaignViewSet, CampaignImageViewSet

router = DefaultRouter()
router.register(r'campaigns', CampaignViewSet, basename='campaign')
router.register(r'campaign-images', CampaignImageViewSet, basename='campaign-image')

urlpatterns = router.urls