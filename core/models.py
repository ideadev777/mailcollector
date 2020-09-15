from django.db import models

# Create your models here.

class Person(models.Model):
    userid = models.CharField(max_length=50)
    nation = models.CharField(max_length=50)
