from django.urls import path

from lib.my_example.education import views

urlpatterns = [
    path('', views.Index.as_view())
]
