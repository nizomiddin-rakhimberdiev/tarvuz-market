from django.urls import path
from .views import create_or_login_view

urlpatterns = [
    path('login/', create_or_login_view, name='login')
]