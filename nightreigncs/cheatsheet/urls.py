from django.urls import path
from . import views

urlpatterns = [
    path('', views.viewer_page, name='cheatsheet'),
]
