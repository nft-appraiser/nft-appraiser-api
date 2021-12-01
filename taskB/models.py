from django.db import models


class TaskB_table(models.Model):
    img = models.ImageField(upload_to='taskB/', default='defo')
    pred_price = models. FloatField()
