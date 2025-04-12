from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import (
    WinnerViewSet,
    WinnerVerificationViewSet,
    WinnerVerificationUpdateViewSet,
    WinnerPrizeUpdateViewSet
)

router = DefaultRouter()
router.register(r'winners', WinnerViewSet, basename='winner')
router.register(r'winner-verifications', WinnerVerificationViewSet, basename='winner-verification')
router.register(r'winner-verification-updates', WinnerVerificationUpdateViewSet, basename='winner-verification-update')
router.register(r'winner-prize-updates', WinnerPrizeUpdateViewSet, basename='winner-prize-update')

urlpatterns = router.urls