from django.shortcuts import render
from django.http.response import JsonResponse
from django.http import HttpResponse
from django.views.decorators.csrf import ensure_csrf_cookie

import json, base64
import sys

import numpy as np
import cv2

sys.path.append("Swin-Transformer-TF")
sys.path.append("task/view.utils")
from utils import *

def Index(request):
    return render(request, 'task/index.html')


def Res(request):
    data = request.body.decode('utf-8')
    jsondata = json.loads(data)

    try:
        # taskB predict
        image_base64 = jsondata['image']
        encoded_data = image_base64.split(',')[1]
        nparr = np.fromstring(base64.b64decode(encoded_data), np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

        model = load_model("task/ml_models/swintransformerB.pkl")
        pred = model.model.predict(cv2.resize(img/255., (224, 224)).reshape(1, 224, 224, 3))[0][0]

        img = cv2.cvtColor(img, cv2.COLOR_RGB2RGBA)
        result, dst_data = cv2.imencode('.png', img)
        dst_base64 = base64.b64encode(dst_data).decode()
        pred = str(pred)

        response = JsonResponse({
                "image": "data:image/png;base64,"+dst_base64,
                "predict": pred,
                "task" : "taskB"
                })

    except:
        # taskA predict
        address = jsondata['address']
        token_id = jsondata['token_id']
        model = load_model('task/ml_models/swintransformerA.pkl')
        img = get_img(address, token_id)
        pred = model.model.predict(cv2.resize(img/255., (224, 224)).reshape(1, 224, 224, 3))[0][0]

        result, dst_data = cv2.imencode('.png', img)
        dst_base64 = base64.b64encode(dst_data).decode()
        pred = str(pred)

        response = JsonResponse({
            "image": "data:image/png;base64,"+dst_base64,
            "predict": pred,
            "task": "taskA"
            })

    return response
