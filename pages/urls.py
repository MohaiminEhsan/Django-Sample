# pages/urls.py

from django.urls import path
from pages import views

urlpatterns = [
    path("", views.home, name='My Home'),
]