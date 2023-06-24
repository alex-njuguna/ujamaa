from django.db import models
from django.contrib.auth.models import User

"""
create model profile:
    user - link to django auth model
    user id - int field
    bio - text field
    image - save in media dir(profile_images dir)
            default img(img filed)
    location - char field  
"""
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField()
    bio = models.TextField(blank=True)
    image = models.ImageField(upload_to='profile_images', default='blank_profile.png')
    location = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.user.username