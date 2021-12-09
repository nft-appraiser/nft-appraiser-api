import sys

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import TaskBForm
from .models import TaskB_table
import cv2
from PIL import Image
from django.conf import settings

sys.path.append("taskB/views_utils")
sys.path.append("Swin-Transformer-TF")
from utils import *


def index(request):
    if request.method == "POST":
        # add predict method
        model = load_model("taskB/swintransformerB.pkl")
        img = Image.open(request.FILES['img'])
        img = cv2.cvtColor(np.array(img), cv2.COLOR_RGBA2BGR)
        pred = model.model.predict(cv2.resize(img/225., (224, 224)).reshape(1, 224, 224, 3))[0][0]
        return render(request, 'taskB/result.html', {'pred': pred})
    else:
        form = TaskBForm(request.POST, request.FILES)
        return render(request, 'taskB/index.html', {'form': form})

