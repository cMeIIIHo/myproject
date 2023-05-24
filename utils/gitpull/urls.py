from django.urls import path
import os
from .gitpull import gitpull


app_name = os.path.basename(os.path.dirname(os.path.realpath(__file__)))  # название прило из пути

urlpatterns = [
    path('gitpull/', gitpull, name='gitpull'),
]
