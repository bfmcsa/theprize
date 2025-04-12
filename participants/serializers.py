from rest_framework import serializers
from .models import Participant, ParticipantAnswer
from campaigns.models import Campaign

class ParticipantAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParticipantAnswer
        fields = ['id', 'question', 'question_ar', 'answer', 'created_at']
        read_only_fields = ['created_at']

class ParticipantSerializer(serializers.ModelSerializer):
    answers = ParticipantAnswerSerializer(many=True, required=False)
    campaign_title = serializers.CharField(source='campaign.title', read_only=True)

    class Meta:
        model = Participant
        fields = [
            'id', 'campaign', 'campaign_title', 'first_name', 'last_name',
            'first_name_ar', 'last_name_ar', 'email', 'phone', 'city', 'country',
            'validation_status', 'validation_notes', 'language', 'agreed_to_terms',
            'answers', 'created_at', 'updated_at'
        ]
        read_only_fields = ['validation_status', 'validation_notes', 'created_at', 'updated_at']

    def validate(self, data):
        campaign = data.get('campaign')
        if campaign and campaign.status != 'active':
            raise serializers.ValidationError("Cannot register for inactive campaigns")
        return data

class ParticipantValidationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participant
        fields = ['validation_status', 'validation_notes']