"""docstring占位符"""
from django.db import models

# Create your models here.


class Item(models.Model):
    """docstring占位符"""
    name = models.CharField(max_length=20)
    item_model = models.CharField(max_length=20)
    unit = models.CharField(max_length=6)
    location = models.CharField(max_length=6)

    def __str__(self):
        return self.name+' '+self.item_model+' '+self.unit


class ItemsIn(models.Model):
    """docstring占位符"""
    item = models.ForeignKey(Item, on_delete=models.DO_NOTHING)
    quantity = models.IntegerField()
    price = models.FloatField()
    total_price = models.FloatField()
    in_date = models.DateField()
    operator = models.CharField(max_length=10)
    is_deleted = models.BooleanField(default=False)


class ItemsOut(models.Model):
    """docstring占位符"""
    item = models.ForeignKey(Item, on_delete=models.DO_NOTHING)
    quantity = models.IntegerField()
    out_date = models.DateField()
    item_user = models.CharField(max_length=10)
    operator = models.CharField(max_length=10)
    is_deleted = models.BooleanField(default=False)


class ItemsTotal(models.Model):
    """docstring占位符"""
    item = models.ForeignKey(Item, on_delete=models.DO_NOTHING)
    quantity = models.IntegerField()
    is_deleted = models.BooleanField(default=False)
