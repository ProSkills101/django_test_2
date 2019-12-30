from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

# Create your models here.
class NBA_Player(models.Model):
  stats_player_id = models.CharField(max_length=100)
  name = models.CharField(max_length=100)
  number = models.IntegerField()
  team = models.CharField(max_length=100)
  created = models.DateTimeField(default=timezone.now)
  updated = models.DateTimeField(default=timezone.now)
  ht = models.FloatField()
  wt = models.FloatField()
  born = models.DateTimeField()
  prior = models.CharField(max_length=100)
  draft = models.CharField(max_length=100)
  exp = models.FloatField()
  pts = models.FloatField()
  reb = models.FloatField()
  ast = models.FloatField()
  pie = models.FloatField()

  def __str__(self):
      return self.name
