
from django.db import models

class UserInfo(models.Model):
    username = models.CharField(max_length=20)
    userid = models.CharField(max_length=20)
    userpw = models.CharField(max_length=20)