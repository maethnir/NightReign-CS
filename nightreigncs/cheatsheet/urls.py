from django.urls import path
from django_distill import distill_path
from . import views

def get_static_args():
    return None

urlpatterns = [
    path('', views.viewer_page, name='cheatsheet'),

    distill_path(
        '',
        views.viewer_page,
        name='index',
        distill_func=get_static_args,
        distill_file='index.html',
    ),
]
