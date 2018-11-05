"""docstring占位"""
from django.contrib import admin
from .models import Item, ItemsIn, ItemsOut, ItemsTotal

# Register your models here.


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    """docstring占位"""
    list_display = ('id', 'name', 'item_model', 'unit', 'location',)


@admin.register(ItemsIn)
class ItemsInAdmin(admin.ModelAdmin):
    """docstring占位"""
    list_display = ('id', 'item', 'quantity', 'price',
                    'in_date', 'operator', 'is_deleted',)


@admin.register(ItemsOut)
class ItemsOutAdmin(admin.ModelAdmin):
    """docstring占位"""
    list_display = ('id', 'item', 'quantity', 'out_date', 'item_user',
                    'operator', 'is_deleted',)


@admin.register(ItemsTotal)
class ItemsTotalAdmin(admin.ModelAdmin):
    """docstring占位"""
    list_display = ('item', 'quantity', 'is_deleted')
