from django.contrib import admin
from .models import UserProfile, Role, Right

admin.site.register(UserProfile)
admin.site.register(Role)
admin.site.register(Right)