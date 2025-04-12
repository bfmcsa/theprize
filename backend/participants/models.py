from django.db import models
from django.utils.translation import gettext_lazy as _
from campaigns.models import Campaign

class Participant(models.Model):
    VALIDATION_STATUS = (
        ('pending', _('Pending')),
        ('valid', _('Valid')),
        ('invalid', _('Invalid')),
    )

    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE, related_name='participants')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    first_name_ar = models.CharField(max_length=100, blank=True)
    last_name_ar = models.CharField(max_length=100, blank=True)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    city = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=100, blank=True)
    validation_status = models.CharField(
        max_length=10,
        choices=VALIDATION_STATUS,
        default='pending'
    )
    validation_notes = models.TextField(blank=True)
    language = models.CharField(
        max_length=10,
        choices=(('en', 'English'), ('ar', 'Arabic')),
        default='en'
    )
    agreed_to_terms = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _('Participant')
        verbose_name_plural = _('Participants')
        ordering = ['-created_at']
        unique_together = [['campaign', 'email'], ['campaign', 'phone']]

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class ParticipantAnswer(models.Model):
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE, related_name='answers')
    question = models.CharField(max_length=255)
    question_ar = models.CharField(max_length=255, blank=True)
    answer = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _('Participant Answer')
        verbose_name_plural = _('Participant Answers')