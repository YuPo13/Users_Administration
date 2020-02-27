from .views import get_index_page
from django.urls import path

app_name = "index_page"

urlpatterns = [
    path('', get_index_page, name='index_page'),
]