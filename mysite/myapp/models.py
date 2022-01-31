from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.ForeignKey(User, related_name="user_profile", on_delete=models.CASCADE)
    first_name = models.TextField(default='')
    last_name = models.TextField(default='')
    email = models.EmailField(default='')
    location = models.TextField(default='')
    landmark = models.TextField(default='')
    locality = models.TextField(default='')
    administrative_area_level_1 = models.TextField(default='')
    postal_code = models.TextField(default='')
    country = models.TextField(default='')
    latitude = models.CharField(max_length=100, default='')
    longitude = models.CharField(max_length=100, default='')
