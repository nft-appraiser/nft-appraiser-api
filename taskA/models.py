from django.db import models


class TaskA_table(models.Model):
    asset_contract_address = models.CharField(max_length=100)
    token_id = models.IntegerField()
    img = models.ImageField(upload_to='taskA/', default='defo')
    pred_price = models.FloatField()
