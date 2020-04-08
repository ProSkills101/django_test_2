from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

# Create your models here.
class Blog(models.Model):
  user = models.ForeignKey(
    get_user_model(),
    on_delete=models.CASCADE, default=None
  )
  title = models.CharField(max_length=20000)
  html = models.CharField(max_length=20000)
  cover = models.CharField(max_length=300, null=True, blank=True)
  created = models.DateTimeField('created', default=timezone.now)
  updated = models.DateTimeField('updated', default=timezone.now)
  state = models.CharField(max_length=200, null=True, blank=True)
  category = models.CharField(max_length=200, null=True, blank=True)

  def __str__(self):
      return self.title