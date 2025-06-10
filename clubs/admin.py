from django.contrib import admin

from .models import Club

class ClubAdmin(admin.ModelAdmin):
    club_display = ('id', 'title', 'is_published', 'dollar_price', 'list_date', 'realtor')
    club_display_links = ('id', 'title')
    club_filter = ('clubfilters add them',)
    club_editable = ('is_published',)
    search_fields = ('title', 'description', 'address', 'city', 'state', 'zipcode', 'price')
    club_per_page = 20

# Register your models here.
admin.site.register(Club, ClubAdmin)