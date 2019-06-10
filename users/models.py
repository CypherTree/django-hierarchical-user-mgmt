from django.contrib.auth.models import AbstractUser
from django.db import models
from .managers import UserManager

class Role(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class User(AbstractUser):
    username = None
    email = models.EmailField( unique=True)
    USERNAME_FIELD = 'email'
    role = models.ManyToManyField(Role)
    category = models.ManyToManyField(Category)
    REQUIRED_FIELDS = ['role']
    objects = UserManager()

    def __str__(self):
        return self.email
