from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.utils import timezone

# Create your models here.
class Question(models.Model):
  user = models.ForeignKey(
    get_user_model(),
    on_delete=models.CASCADE, default=None, null = True
  )
  question_text = models.CharField(max_length=200)
  created = models.DateTimeField('created', default=timezone.now)
  updated = models.DateTimeField('updated', default=timezone.now)
  state = models.CharField(max_length=200, null=True)

  def __str__(self):
      return self.question_text

class Choice(models.Model):
  user = models.ForeignKey(
    get_user_model(),
    on_delete=models.CASCADE, default=None, null = True
  )
  question = models.ForeignKey(Question, on_delete=models.CASCADE)
  choice_text = models.CharField(max_length=200)
  #votes = models.IntegerField(default=0)
  created = models.DateTimeField('created', default=timezone.now)
  updated = models.DateTimeField('updated', default=timezone.now)

  def __str__(self):
      return self.choice_text

class Vote(models.Model):
  user = models.ForeignKey(
    get_user_model(),
    on_delete=models.CASCADE, default=None, null = True
  )
  question = models.ForeignKey(Question, on_delete=models.CASCADE)
  choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
  created = models.DateTimeField('created', default=timezone.now)
  updated = models.DateTimeField('updated', default=timezone.now)