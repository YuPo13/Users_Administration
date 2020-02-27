from django.db import models
from django.contrib.auth.models import User

MAX_STATUS_LENGTH = 500


class Right(models.Model):
    right = models.CharField(primary_key=True, max_length=MAX_STATUS_LENGTH)


class Role(models.Model):
    role = models.CharField(primary_key=True, max_length=MAX_STATUS_LENGTH)
    rights = models.ManyToManyField(Right, related_name='roles')


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    role = models.OneToOneField(Role, on_delete=models.CASCADE, null=True)
