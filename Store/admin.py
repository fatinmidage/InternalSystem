from django.contrib import admin
from .models import Item, Items_in, Items_out, Items_Total

# Register your models here.


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('id',  'name', 'item_model','unit', )


@admin.register(Items_in)
class Items_inAdmin(admin.ModelAdmin):
    list_display = ('id', 'item', 'quantity', 'price',
                    'in_date', 'operator', 'location', 'is_deleted',)


@admin.register(Items_out)
class Items_outAdmin(admin.ModelAdmin):
    list_display = ('id', 'item', 'quantity', 'out_date',
                    'operator', 'location', 'is_deleted',)


@admin.register(Items_Total)
class Items_TotalAdmin(admin.ModelAdmin):
    list_display = ('item', 'quantity', 'is_deleted')
