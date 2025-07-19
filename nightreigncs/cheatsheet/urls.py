from django.urls import path
from django_distill import distill_path
from . import views

def get_static_args():
    yield None  # Only one version of the page

urlpatterns = [
    path('', views.viewer_page, name='cheatsheet'),
    distill_path('', views.viewer_page, name='distilled_cheatsheet', distill_func=get_static_args),
]
