import sys

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import TaskAForm
from .models import TaskA_table
import cv2
from django.conf import settings

sys.path.append("taskA/views_utils")
sys.path.append("Swin-Transformer-TF")
from utils import *


def index(request):
    if request.method == "POST":
        # add predict process
        model = load_model('taskA/swintransformerA.pkl')
        return render(request, 'taskA/result.html', {'pred': 0})
    else:   
        form = TaskAForm(request.POST, request.FILES)
        return render(request, 'taskA/index.html', {'form': form})

