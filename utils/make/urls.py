from django.urls import path
import os
from .make import make

app_name = os.path.basename(os.path.dirname(os.path.realpath(__file__)))  # название прило из пути

urlpatterns = [
    path('make/', make, name='make'),
]
