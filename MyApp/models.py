from django.db import models

# Create your models here.

# Admin class for the admin_login user
class Admin:
    email: str
    password: str

# User class for the ip details database
class user(models.Model):
    ip = models.CharField(max_length=20)
    city = models.CharField(max_length=20, primary_key=True)
    state = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    count = models.IntegerField(default=0)
    date = models.CharField(max_length=20)
    time = models.CharField(max_length=20)

    objects = models.Manager()
