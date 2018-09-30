from django.db import models

# Create your models here.

class Knowte(models.Model):
  text = models.CharField(max_length=8192)