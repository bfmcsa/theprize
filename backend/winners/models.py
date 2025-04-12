from django.db import models
from django.utils.translation import gettext_lazy as _
from campaigns.models import Campaign
from participants.models import Participant

class Winner(models.Model):
    VERIFICATION_STATUS = (
        ('pending', _('Pending')),
        ('verified', _('Verified')),
        ('rejected', _('Rejected')),
    )

    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE, related_name='winners')
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE, related_name='wins')
    selected_at = models.DateTimeField(auto_now_add=True)
    verification_status = models.CharField(
        max_length=10,
        choices=VERIFICATION_STATUS,
        default='pending'
    )
    verification_notes = models.TextField(blank=True)
    prize_claimed = models.BooleanField(default=False)
    prize_claimed_at = models.DateTimeField(null=True, blank=True)
    prize_delivered = models.BooleanField(default=False)
    prize_delivered_at = models.DateTimeField(null=True, blank=True)
    delivery_notes = models.TextField(blank=True)

    class Meta:
        verbose_name = _('Winner')
        verbose_name_plural = _('Winners')
        ordering = ['-selected_at']
        unique_together = ['campaign', 'participant']

    def __str__(self):
        return f"{self.participant} - {self.campaign}"

class WinnerVerification(models.Model):
    winner = models.ForeignKey(Winner, on_delete=models.CASCADE, related_name='verifications')
    verification_method = models.CharField(max_length=50)
    verification_code = models.CharField(max_length=100, blank=True)
    verification_attempts = models.PositiveIntegerField(default=0)
    last_attempt_at = models.DateTimeField(null=True, blank=True)
    is_successful = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _('Winner Verification')
        verbose_name_plural = _('Winner Verifications')