from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField


class CustomAccountManager(BaseUserManager):
    def create_superuser(self, email, user_name, password, **other_fields):
        other_fields.setdefault('is_active', True)
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        if other_fields.get('is_staff') is not True:
            raise ValueError('Superuser must be assigned is_staff=True status')
        if other_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must be assigned is_superuser=True status')
        return self.create_superuser(email, user_name, password, **other_fields)

    def create_user(self, email, user_name, password, **other_fields):
        if not email:
            raise ValueError('You must enter an email address')
        email = self.normalize_email(email)
        user = self.models(email=email, user_name=user_name, password=password, **other_fields)
        user.set_password(password)
        user.save()
        return user


class UserBase(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("email"), unique=True)
    user_name = models.CharField(max_length=100, unique=True)
    full_name = models.CharField(max_length=250)
    about = models.TextField(blank=True)
    # Delivery Details
    Address_line1 = models.CharField(max_length=150, blank=True)
    Address_line2 = models.CharField(max_length=150, blank=True)
    country = CountryField(default='Ghana')
    phone = models.CharField(max_length=18)
    # user status
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    object = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name']

    class Meta:
        verbose_name = 'Accounts'
        verbose_name_plural = 'Accounts'

    def __str__(self):
        return self.user_name
