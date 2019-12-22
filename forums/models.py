from django.db import models

# Create your models here.from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

# Create your models here.
class Forum(models.Model):
  user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
  title = models.CharField(max_length=200)
  html = models.CharField(max_length=30000, default='')
  created = models.DateTimeField('created', default=timezone.now)
  updated = models.DateTimeField('updated', default=timezone.now)
  state = models.CharField(max_length=200, blank=True)
  tag = models.CharField(max_length=200, blank=True)

  def __str__(self):
      return self.title

class Topic(models.Model):
  user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
  forum = models.ForeignKey(Forum, on_delete=models.CASCADE)
  title = models.CharField(max_length=200)
  html = models.CharField(max_length=30000, default='')
  created = models.DateTimeField('created', default=timezone.now)
  updated = models.DateTimeField('updated', default=timezone.now)
  state = models.CharField(max_length=200, blank=True)
  tag = models.CharField(max_length=200, blank=True)

  def __str__(self):
      return self.title

class Post(models.Model):
  user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
  topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
  html = models.CharField(max_length=30000)
  created = models.DateTimeField('created', default=timezone.now)
  updated = models.DateTimeField('updated', default=timezone.now)
  state = models.CharField(max_length=200, blank=True)
  tag = models.CharField(max_length=200, blank=True)

  def __str__(self):
      return self.html

class Comment(models.Model):
  user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
  topic = models.ForeignKey(Topic, on_delete=models.CASCADE, default=None)
  post = models.ForeignKey(Post, on_delete=models.CASCADE, default=None)
  text = models.CharField(max_length=1000)
  created = models.DateTimeField('created', default=timezone.now)
  updated = models.DateTimeField('updated', default=timezone.now)
  state = models.CharField(max_length=200, blank=True)
  tag = models.CharField(max_length=200, blank=True)

  def __str__(self):
      return self.text
