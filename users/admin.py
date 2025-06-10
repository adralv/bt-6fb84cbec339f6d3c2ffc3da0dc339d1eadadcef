from django.contrib import admin
from .models import UserProfile

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'graduation_year')
    search_fields = ('user__username', 'user__email')
    list_filter = ('graduation_year',)
