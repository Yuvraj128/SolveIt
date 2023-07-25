from django.db import models
from datetime import datetime

# Create your models here.
class Profile(models.Model):
    username = models.CharField(max_length=50)
    profile_img = models.ImageField(upload_to='profile_image')
    
    def __str__(self) -> str:
        return self.username
    
    
class Messages(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    message = models.CharField(max_length=250)
    timing = models.TimeField(default=datetime.now())
    
    
    def __str__(self) -> str:
        return str(self.id)+" "+self.message
    