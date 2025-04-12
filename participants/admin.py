from django.contrib import admin
from .models import Participant, ParticipantAnswer

class ParticipantAnswerInline(admin.TabularInline):
    model = ParticipantAnswer
    extra = 1

@admin.register(Participant)
class ParticipantAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'campaign', 'validation_status')
    list_filter = ('validation_status', 'campaign', 'language')
    search_fields = ('first_name', 'last_name', 'email', 'phone')
    inlines = [ParticipantAnswerInline]
    fieldsets = (
        (None, {
            'fields': ('campaign', 'first_name', 'last_name', 'first_name_ar', 'last_name_ar')
        }),
        ('Contact Info', {
            'fields': ('email', 'phone', 'city', 'country')
        }),
        ('Validation', {
            'fields': ('validation_status', 'validation_notes')
        }),
        ('Settings', {
            'fields': ('language', 'agreed_to_terms')
        }),
    )

admin.site.register(ParticipantAnswer)