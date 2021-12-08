import sys
sys.path.append("views_utils")

from django.urls import path
from . import views


app_name = 'taskA'
urlpatterns = [
    path('index/', views.index, name='index'),
]
