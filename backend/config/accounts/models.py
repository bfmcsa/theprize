from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    USER_TYPE_CHOICES = (
        ('admin', _('Administrator')),
        ('company', _('Company User')),
    )
    user_type = models.CharField(
        max_length=10,
        choices=USER_TYPE_CHOICES,
        default='company'
    )
    phone = models.CharField(max_length=20, blank=True)
    language = models.CharField(
        max_length=10,
        choices=(('en', 'English'), ('ar', 'Arabic')),
        default='en'
    )

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')

class Company(models.Model):
    name = models.CharField(max_length=255)
    name_ar = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    description_ar = models.TextField(blank=True)
    logo = models.ImageField(upload_to='company_logos/', blank=True)
    website = models.URLField(blank=True)
    contact_email = models.EmailField()
    contact_phone = models.CharField(max_length=20)
    users = models.ManyToManyField(User, related_name='companies')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _('Company')
        verbose_name_plural = _('Companies')

    def __str__(self):
        return self.name