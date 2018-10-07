from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager, PermissionsMixin)

# Create your models here.

class UserProfileManager(BaseUserManager):
    # Helps django work with our custom model

    def create_user(self, email, name, password=None):
        # Create a new user profile object

        if not email:
            raise ValueError('Users must have an email address.')

        email = self.normalize_email(email)
        user = self.model(email = email, name = name)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        # Creates and saves a new superuser with given details
        user = self.create_user(email, name, password)
        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    # Represent user profile inside our system

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_fullname(self):
        # Used to get a users full name
        return self.name

    def get_shortname(self):
        # Used to get a users short name
        return self.name

    def __str__(self):
        # Convert object to string and return it
        return self.email
