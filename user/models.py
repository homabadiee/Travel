from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone


class UserManager(BaseUserManager):

    def create_user(self, email, user_name, phone, password,  **extra_fields):

        if not email:
            raise ValueError(_('You must provide email address'))


        email = self.normalize_email(email)
        user = self.model(email=email, user_name=user_name, phone=phone, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, user_name, phone, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        return self.create_user(email, user_name, phone, password, **extra_fields)



class PassengerUser(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    user_name = models.CharField(max_length=50, null=True)
    email = models.EmailField(_('email address'), unique=True, null=True)
    phone = models.CharField(max_length=12, null=True)
    address = models.CharField(max_length=200, null=True)
    birthDate = models.DateField(null=True)
    gender = models.CharField(max_length=6, null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name', 'phone']

    def __str__(self):
        return self.email
