from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError

def file_size(value):
    limit = 300 * 1024  # 300kb
    if value.size > limit:
        raise ValidationError('File too large.')

def filePath(instance, filename):
    return '{}/{}'.format(instance.username, filename)

class User(AbstractUser):
  nickname = models.CharField(max_length=50, blank=True)
  avatar = models.FileField(upload_to=filePath, validators=[file_size], blank=True)
  text = models.TextField(max_length=500, blank=True)
# Create your models here.



