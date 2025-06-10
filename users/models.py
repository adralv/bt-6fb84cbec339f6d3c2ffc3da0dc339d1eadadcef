from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    graduation_year = models.IntegerField()
    profile_picture = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
