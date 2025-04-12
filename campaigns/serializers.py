from rest_framework import serializers
from .models import Campaign, CampaignImage

class CampaignImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CampaignImage
        fields = ['id', 'image', 'caption', 'caption_ar', 'is_primary', 'created_at']
        read_only_fields = ['created_at']

class CampaignSerializer(serializers.ModelSerializer):
    images = CampaignImageSerializer(many=True, read_only=True)
    company_name = serializers.CharField(source='company.name', read_only=True)

    class Meta:
        model = Campaign
        fields = [
            'id', 'company', 'company_name', 'title', 'title_ar',
            'description', 'description_ar', 'start_date', 'end_date',
            'prize_name', 'prize_name_ar', 'prize_description', 'prize_description_ar',
            'terms_conditions', 'terms_conditions_ar', 'status',
            'max_participants', 'is_public', 'images', 'created_at', 'updated_at'
        ]
        read_only_fields = ['created_at', 'updated_at']

    def validate(self, data):
        if data['start_date'] > data['end_date']:
            raise serializers.ValidationError("End date must be after start date")
        return data