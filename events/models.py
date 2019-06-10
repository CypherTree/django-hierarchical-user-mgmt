from django.conf import settings # never write `from django.conf.settings import ...`
from django.db import models

# Create your models here.

class Event(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(blank=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    location =  models.CharField(max_length=255)
