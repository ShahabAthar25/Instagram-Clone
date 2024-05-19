from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator
from django.utils.translation import gettext as _
from django.db import models

from .managers import CustomUserManager

class User(AbstractUser):
    email = models.EmailField(_('Email Address'), unique=True)
    first_name = models.CharField(_('First Name'), max_length=150)
    last_name = models.CharField(_('Last Name'), max_length=150)
    profile_pic = models.ImageField(_('Profile Picture'), upload_to="users/", blank=True, null=True)
    website = models.URLField(_('Website'), max_length=200, validators=[MinLengthValidator(10)], blank=True, null=True)
    bio = models.CharField(_('Bio'), max_length=150, validators=[MinLengthValidator(1)], blank=True, null=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ('email', 'first_name', 'last_name')
    
    objects = CustomUserManager()

    def __str__(self):
        return f"{self.username}"