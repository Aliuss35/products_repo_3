from email.policy import default
from tkinter import CASCADE
from django.db import models

from stores.models import Stores

# Create your models here.
class Product(models.Model):
  name = models.CharField(max_length=150)
  price = models.IntegerField()
  in_stock = models.BooleanField(default=True)
  condition = models.CharField(max_length=150, default="New")
  stores = models.ForeignKey(Stores, on_delete=models.CASCADE, null=True)