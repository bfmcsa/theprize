from rest_framework import serializers
from .models import Winner, WinnerVerification
from participants.serializers import ParticipantSerializer
from campaigns.serializers import CampaignSerializer

class WinnerVerificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = WinnerVerification
        fields = ['id', 'verification_method', 'verified_by', 'notes', 'created_at']
        read_only_fields = ['created_at']

class WinnerSerializer(serializers.ModelSerializer):
    participant = ParticipantSerializer(read_only=True)
    campaign = CampaignSerializer(read_only=True)
    verifications = WinnerVerificationSerializer(many=True, read_only=True)

    class Meta:
        model = Winner
        fields = [
            'id', 'campaign', 'participant', 'selected_at',
            'verification_status', 'verification_notes',
            'prize_claimed', 'prize_claimed_at',
            'prize_delivered', 'prize_delivered_at',
            'delivery_notes', 'verifications'
        ]
        read_only_fields = [
            'selected_at', 'verification_status',
            'verification_notes', 'prize_claimed_at',
            'prize_delivered_at'
        ]

class WinnerVerificationUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Winner
        fields = ['verification_status', 'verification_notes']

class WinnerPrizeUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Winner
        fields = ['prize_claimed', 'prize_delivered', 'delivery_notes']