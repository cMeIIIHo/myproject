from django.urls import path
import os
from .webhook import webhook

app_name = os.path.basename(os.path.dirname(os.path.realpath(__file__)))  # название прило из пути

urlpatterns = [
    path("webhook", webhook),
]
