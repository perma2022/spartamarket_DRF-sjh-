from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    name = models.CharField(max_length=30)
    nickname = models.CharField(max_length=30)
    birthday = models.DateField()

    REQUIRED_FIELDS = ['name', 'nickname', 'birthday']
    #강제인식
# Create your models here.
