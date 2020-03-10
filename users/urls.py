from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import user_registration, user_login, user_profile, own_password_change, others_password_change, new_user_creation

app_name = "users"

urlpatterns = [
    path('registration', user_registration, name='registration'),
    path('login', user_login, name='login'),
    path('logout', LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('profile_mgr/<uuid>', user_profile, name='profile'),
    path('profile/<uuid>', user_profile, name='profile'),
    path('own_password_change', own_password_change, name='own_password_change'),
    path('<other_user_uuid>/others_password_change', others_password_change, name='others_password_change'),
    path('creation', new_user_creation, name='creation'),
]