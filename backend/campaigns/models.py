from django.db import models
from django.utils.translation import gettext_lazy as _
from accounts.models import Company

class Campaign(models.Model):
    STATUS_CHOICES = (
        ('draft', _('Draft')),
        ('active', _('Active')),
        ('completed', _('Completed')),
        ('cancelled', _('Cancelled')),
    )

    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='campaigns')
    title = models.CharField(max_length=255)
    title_ar = models.CharField(max_length=255, blank=True)
    description = models.TextField()
    description_ar = models.TextField(blank=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    prize_name = models.CharField(max_length=255)
    prize_name_ar = models.CharField(max_length=255, blank=True)
    prize_description = models.TextField()
    prize_description_ar = models.TextField(blank=True)
    terms_conditions = models.TextField()
    terms_conditions_ar = models.TextField(blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    max_participants = models.PositiveIntegerField(null=True, blank=True)
    is_public = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _('Campaign')
        verbose_name_plural = _('Campaigns')
        ordering = ['-created_at']

    def __str__(self):
        return self.title

class CampaignImage(models.Model):
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='campaign_images/')
    caption = models.CharField(max_length=255, blank=True)
    caption_ar = models.CharField(max_length=255, blank=True)
    is_primary = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _('Campaign Image')
        verbose_name_plural = _('Campaign Images')