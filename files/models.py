from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError

def file_size(value): # add this to some file where you can import it from
  limit = 1024 * 1024
  if value.size > limit:
      raise ValidationError('File too large.')

def filePath(instance, filename):
  return '{}/{}'.format(instance.user.username, filename)

class File(models.Model):
  user = models.ForeignKey(
    get_user_model(),
    on_delete=models.CASCADE, default=None
  )
  name = models.CharField(max_length=200, blank=True, null=True)
  album = models.CharField(max_length=200, blank=True, null=True)
  desc = models.CharField(max_length=500, blank=True, null=True)
  created = models.DateTimeField('created', default=timezone.now)
  file = models.FileField(upload_to=filePath, validators=[file_size])
  type = models.CharField(max_length=100, blank=True, null=True)
  tag = models.CharField(max_length=100, blank=True, null=True)

  def __str__(self):
    return self.name

