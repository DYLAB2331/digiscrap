from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Photo(models.Model):
    users = models.ManyToManyField(User, through="UserPhotoThroughRelation")
    image = models.ImageField(upload_to="photos/")
    description = models.TextField()
    date = models.DateField()

class UserPhotoThroughRelation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE)

