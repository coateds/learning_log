"""Defines URL patterns for users"""
from django.urls import path
# from django.contrib.auth.views import login
from django.contrib.auth.views import LoginView

from . import views

app_name = 'users'
urlpatterns = [
    # Login page
    path('login/', LoginView, {'template_name': 'users/login.html'}, name='LoginView'),
]

