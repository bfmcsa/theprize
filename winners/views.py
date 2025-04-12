from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from .models import Winner, WinnerVerification
from .serializers import (
    WinnerSerializer, 
    WinnerVerificationSerializer,
    WinnerVerificationUpdateSerializer,
    WinnerPrizeUpdateSerializer
)
from campaigns.models import Campaign
from participants.models import Participant

class WinnerViewSet(viewsets.ModelViewSet):
    queryset = Winner.objects.all()
    serializer_class = WinnerSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset()
        campaign_id = self.request.query_params.get('campaign_id')
        if campaign_id:
            queryset = queryset.filter(campaign_id=campaign_id)
        return queryset

    def create(self, request, *args, **kwargs):
        campaign_id = request.data.get('campaign')
        participant_id = request.data.get('participant')
        
        try:
            campaign = Campaign.objects.get(id=campaign_id)
            participant = Participant.objects.get(id=participant_id)
            
            if not participant.campaign == campaign:
                return Response(
                    {"error": "Participant does not belong to this campaign"},
                    status=status.HTTP_400_BAD_REQUEST
                )
                
            winner = Winner.objects.create(
                campaign=campaign,
                participant=participant
            )
            serializer = self.get_serializer(winner)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
            
        except (Campaign.DoesNotExist, Participant.DoesNotExist):
            return Response(
                {"error": "Invalid campaign or participant ID"},
                status=status.HTTP_400_BAD_REQUEST
            )

class WinnerVerificationViewSet(viewsets.ModelViewSet):
    queryset = WinnerVerification.objects.all()
    serializer_class = WinnerVerificationSerializer
    permission_classes = [permissions.IsAdminUser]

class WinnerVerificationUpdateViewSet(viewsets.ModelViewSet):
    queryset = Winner.objects.all()
    serializer_class = WinnerVerificationUpdateSerializer
    permission_classes = [permissions.IsAdminUser]

class WinnerPrizeUpdateViewSet(viewsets.ModelViewSet):
    queryset = Winner.objects.all()
    serializer_class = WinnerPrizeUpdateSerializer
    permission_classes = [permissions.IsAdminUser]