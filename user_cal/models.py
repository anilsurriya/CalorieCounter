from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class User_cal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    height = models.IntegerField()
    weight = models.DecimalField(decimal_places=2, max_digits=5)
    age = models.IntegerField()