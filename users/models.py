from django.db import models
from django_crm_template.settings import MAX_STATUS_LENGTH


class Rights(models.Model):
    right = models.CharField(primary_key=True, max_length=MAX_STATUS_LENGTH)


class Roles(models.Model):
    role = models.CharField(primary_key=True, max_length=MAX_STATUS_LENGTH)
    rights = models.ManyToManyField(Rights, related_name='roles')


class Users(models.Model):
    user_id = models.IntegerField(primary_key=True)
    user_name = models.CharField(max_length=MAX_STATUS_LENGTH, null=True)
    user_surname = models.CharField(max_length=MAX_STATUS_LENGTH, null=True)
    user_email = models.EmailField(unique=True)
    user_registration_date = models.DateTimeField(auto_now_add=True, db_index=True)
    role = models.OneToOneField(Roles, on_delete=models.CASCADE, null=True)
