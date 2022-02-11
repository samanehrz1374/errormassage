from django.db import models

# Create your models here.
class erormsg(models.Model):
    name=models.CharField(max_length=100)
    family=models.CharField(max_length=100)

    