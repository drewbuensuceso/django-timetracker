from django.urls import path
from .views import create_project, delete_project

urlpatterns = [
    path('create_project/', create_project, name='create_project'),
    path('delete_project/', delete_project, name='delete_project'),
]