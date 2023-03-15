from django.db import models

# Create your models here.
class Stores(models.Model):
  name = models.CharField(max_length=255)
  city = models.CharField(max_length=255)