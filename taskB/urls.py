from django.urls import path
from . import views

app_name = 'taskB'
urlpatterns = [
    path('index/', views.index, name='index')
]
