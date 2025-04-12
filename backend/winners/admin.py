from django.contrib import admin
from .models import Winner, WinnerVerification

class WinnerVerificationInline(admin.TabularInline):
    model = WinnerVerification
    extra = 1

@admin.register(Winner)
class WinnerAdmin(admin.ModelAdmin):
    list_display = ('participant', 'campaign', 'selected_at', 'verification_status', 'prize_claimed')
    list_filter = ('verification_status', 'prize_claimed', 'prize_delivered')
    search_fields = ('participant__first_name', 'participant__last_name', 'participant__email')
    inlines = [WinnerVerificationInline]
    fieldsets = (
        (None, {
            'fields': ('campaign', 'participant')
        }),
        ('Verification', {
            'fields': ('verification_status', 'verification_notes')
        }),
        ('Prize Status', {
            'fields': ('prize_claimed', 'prize_claimed_at', 'prize_delivered', 'prize_delivered_at', 'delivery_notes')
        }),
    )

admin.site.register(WinnerVerification)