from django.db import models

class Archive (models.Model):
    type = models.IntegerField()
    date = models.CharField(max_length=150)
    value = models.IntegerField()
    cpf = models.CharField(max_length=150)
    card = models.CharField(max_length=150)
    hour = models.CharField(max_length=150)
    store_owner = models.CharField(max_length=150)
    store_name = models.CharField(max_length=150)