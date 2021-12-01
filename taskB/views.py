from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import TaskBForm
from .models import TaskB_table
import cv2
from django.conf import settings

def index(request):
    if request.method == "POST":
        # add predict method
        return render(request, 'taskB/result.html', {'pred': 0})
    else:
        form = TaskBForm(request.POST, request.FILES)
        return render(request, 'taskB/index.html', {'form': form})

