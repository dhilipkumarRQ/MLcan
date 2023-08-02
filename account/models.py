from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import UserManager
from meta.models import Account_Type


class User(AbstractUser):
    username = None
    first_name = None
    last_name = None
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254, unique=True)
    phone = models.CharField(max_length=10, unique=True)
    password = models.CharField(max_length=300,)
    active_state = models.BooleanField(default=True)
    user_type = models.ForeignKey(Account_Type, on_delete=models.SET_NULL, null=True)
    created_datetime = models.DateTimeField(auto_now_add=True)
    modified_datetime = models.DateTimeField(auto_now=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    objects = UserManager()
