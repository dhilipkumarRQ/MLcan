from django.contrib.auth.base_user import BaseUserManager
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, **extra_fields):
        if not "email" in extra_fields.keys():
            raise ValueError("Email not found")
        if not "password" in extra_fields.keys():
            raise ValueError("Password not found")

        password = extra_fields.get("password")
        extra_fields["email"] = self.normalize_email(extra_fields.get("email"))
        try:
            user = self.model(**extra_fields)
        except Exception as e:
            print(e)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, **extra_fields):
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_staff", True)

        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")

        return self.create_user(**extra_fields)


