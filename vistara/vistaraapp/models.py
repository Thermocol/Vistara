from django.core import validators
from django.core.exceptions import ImproperlyConfigured
from django.db import models
from django.db.models.base import Model
from django.db.models.fields import DateField
from django.utils import timezone
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import User

class videoes(models.Model):
    uploader=models.ForeignKey(User, on_delete=models.CASCADE)
    title= models.CharField(max_length=100)
    description = models.TextField()
    video_file=models.FileField(upload_to='uploads/video' , validators=[FileExtensionValidator(allowed_extensions=['mp4','mkv','avi'])])
    thumbnail=models.FileField(upload_to='uploads/thumbnail')
    Date_posted=models.DateTimeField(default=timezone.now)

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video = models.ForeignKey('videoes', on_delete=models.CASCADE)
    comment = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'User: {self.user} | Created On: {self.created_on.strftime("%b %d %Y %I:%M %p")}'

    