from django.db import models
import uuid
from django.contrib.auth.models import User


class UserProfile(models.Model):
    unique_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    user_manager = models.Manager()
