from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("1/", views.v1, name="v1")
]

