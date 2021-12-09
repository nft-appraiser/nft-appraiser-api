from django.db import models


class TaskA_table(models.Model):
    asset_contract_address = models.CharField(max_length=100)
    token_id = models.IntegerField()
    pred_price = models.FloatField()
