from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Company

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'user_type', 'language', 'is_staff')
    list_filter = ('user_type', 'language', 'is_staff')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'phone')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
        ('Custom fields', {'fields': ('user_type', 'language')}),
    )

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact_email', 'contact_phone', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'contact_email')
    filter_horizontal = ('users',)

admin.site.register(User, CustomUserAdmin)