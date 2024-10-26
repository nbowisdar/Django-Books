from django.urls import path

from . import views

app_name = "books"

urlpatterns = [
    path("home", views.home, name="home"),
]
