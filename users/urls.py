from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import user_registration, user_login, user_profile

app_name = "users"

urlpatterns = [
    path('registration', user_registration, name='registration'),
    path('login', user_login, name='login'),
    path('logout', LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('profile/<username>', user_profile, name='profile'),
]