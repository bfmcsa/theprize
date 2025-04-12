from django.contrib import admin
from .models import Campaign, CampaignImage

class CampaignImageInline(admin.TabularInline):
    model = CampaignImage
    extra = 1

@admin.register(Campaign)
class CampaignAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'start_date', 'end_date', 'status')
    list_filter = ('status', 'start_date', 'end_date')
    search_fields = ('title', 'company__name')
    inlines = [CampaignImageInline]
    fieldsets = (
        (None, {
            'fields': ('company', 'title', 'title_ar', 'description', 'description_ar')
        }),
        ('Dates', {
            'fields': ('start_date', 'end_date')
        }),
        ('Prize Info', {
            'fields': ('prize_name', 'prize_name_ar', 'prize_description', 'prize_description_ar')
        }),
        ('Settings', {
            'fields': ('status', 'max_participants', 'is_public', 'terms_conditions', 'terms_conditions_ar')
        }),
    )

admin.site.register(CampaignImage)