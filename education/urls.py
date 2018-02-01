from django.contrib import admin
from django.urls import path

from education import views

urlpatterns = [
    path('', views.Index.as_view())
]
