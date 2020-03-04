from django.contrib import admin
from .models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

admin.site.unregister(User)


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        is_superuser = request.user.is_superuser

        if not is_superuser:
            disabled_fields = {
                'is_superuser',
            }

            for field_ in disabled_fields:
                if field_ in form.base_fields:
                    form.base_fields[field_].disabled = True

        return form


admin.site.register(UserProfile)
