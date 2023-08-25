from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager
# Create your models here.


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(primary_key=True,unique=True)
    f_name = models.CharField(max_length=50)
    l_name = models.CharField(max_length=50)
    phone  = models.CharField(max_length=14)

    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
