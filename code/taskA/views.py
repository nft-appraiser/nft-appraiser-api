import sys
import base64
import io

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
        address = request.POST['asset_contract_address']
        token_id = request.POST['token_id']
        img = get_img(address, token_id)
        pred = model.model.predict(cv2.resize(img/225., (224, 224)).reshape(1, 224, 224, 3))[0][0]
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGBA)

        img = Image.fromarray(img)
        buf = io.BytesIO()
        img.save(buf, format="PNG")
        base_64img = base64.b64encode(buf.getvalue()).decode().replace("'", "")
        
        return render(request, 'taskA/result.html', {'pred': pred, 'img': base_64img})
    else:   
        form = TaskAForm(request.POST, request.FILES)
        return render(request, 'taskA/index.html', {'form': form})

