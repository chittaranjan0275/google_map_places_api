from django.contrib import admin

# Register your models here.
from myapp.models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    list_display = (
        'user', 'first_name', 'last_name', 'email', 'location', 'landmark', 'locality', 'administrative_area_level_1',
        'postal_code', 'country', 'longitude', 'latitude')
    pass

admin.site.register(UserProfile, UserProfileAdmin)
