from django.db import models
import uuid
from django.contrib.auth.models import User


class UserProfile(models.Model):
    unique_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    user_manager = models.Manager()

    def get_others(self):
        from django.db import connection
        query = f"SELECT id FROM auth_user"
        with connection.cursor() as cursor:
            cursor.execute(query)
            other_users = [User.objects.get(id=id_[0]) for id_ in cursor.fetchall()]

        return other_users
