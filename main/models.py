from django.db import models

# Create your models here.
class Carousel(models.Model):
    title = models.CharField(max_length=50)
    text = models.CharField(max_length=200)
    btn_text = models.CharField(max_length=10)
    align_type = models.CharField(max_length=10)
    img_path = models.CharField(default='', max_length=100)
    pub_date = models.DateTimeField('date published')

class Notice(models.Model):
    title = models.CharField(max_length=50)
    text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
