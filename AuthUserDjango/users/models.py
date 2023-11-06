from django.db import models
from django.utils import timezone

class User(models.Model):
    username = models.CharField(max_length = 10, null=True)
    password = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length= 100, default="example@example.com")
    created_at = models.DateTimeField(default=timezone.now)


# Create your models here.
