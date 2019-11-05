from django.db import models

class SentoData(models.Model):
    r_date = models.DateField('日付')
    author = models.CharField('行った人',max_length=15)
    sento_name = models.CharField('銭湯名',max_length=15)
    sauna = models.BooleanField('サウナ有無',null=False)
    outdoor_bath = models.BooleanField('露天風呂',null=False)
    basic_charge = models.IntegerField('基本料金',null=False)
    station = models.CharField('最寄り駅',max_length=20)
    text = models.TextField('感想')
