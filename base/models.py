from django.db import models
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.


class User(AbstractBaseUser):
    username = models.CharField(unique=True, max_length=16)
    firebase_device_id = models.CharField(max_length=2048, null=True, blank=True)
    encrypted_password = models.CharField(max_length=4096, null=True, blank=True)

    USERNAME_FIELD = "username"

    def get_short_name(self):
        return self.username

    def get_full_name(self):
        return self.username

    def __str__(self):
        return self.username
