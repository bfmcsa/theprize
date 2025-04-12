from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ParticipantViewSet, ParticipantAnswerViewSet, ParticipantValidationViewSet

router = DefaultRouter()
router.register(r'participants', ParticipantViewSet, basename='participant')
router.register(r'participant-answers', ParticipantAnswerViewSet, basename='participant-answer')
router.register(r'participant-validations', ParticipantValidationViewSet, basename='participant-validation')

urlpatterns = router.urls