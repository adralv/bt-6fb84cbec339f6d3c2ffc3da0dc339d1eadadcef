from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager

# from events.models import Event

# Create your models here.
class Club(models.Model):
    club_name= models.CharField(max_length=100)
    club_members = models.ManyToManyField(User, blank=True, related_name='clubs')
    description = models.TextField(blank=True)
    room_number = models.IntegerField()
    image = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    email= models.EmailField(max_length=250)
    teacher=models.CharField(max_length=100, default='null')
    meeting_day=models.TextField(blank=True)
    tags = TaggableManager()

    # announcments= models.ManyToManyField
    def __str__(self):
        return self.club_name
    
    
    
    # actvities=models.ArrayField(base_field=)

    
