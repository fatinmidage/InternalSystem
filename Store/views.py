"""定义处理函数"""

from django.shortcuts import render
from django.http import request
from django.shortcuts import get_object_or_404
from .models import Items_Total, Items_in, Item

# Create your views here.


def storelist(request):
    """docstring占位"""
    store = Items_Total.objects.all()
    context = {}
    context['store'] = store
    return render(request, 'storelist.html', context)


def details_in(request):
    """docstring占位"""
    dt_in = Items_in.objects.all()
    context = {}
    context['items'] = dt_in
    return render(request, 'items_in.html', context)


def add_items_in(it_object: Item, it_info: {}):
    """添加一个入库记录"""
    it_in = Items_in()
    it_in.item = it_object
    it_in.quantity = it_info['quantity']
    it_in.price = it_info['price']
    it_in.total_price = it_in.quantity * it_in.price
    it_in.in_date = it_info['in_date']
    it_in.operator = it_info['operator']
    it_in.save()


def add_items_total(item: Item, it_info: {}):
    """总表插入记录"""
    pass


def add_items_to_intable(request):
    """新增库存"""
    print(request.POST.get('operator'))

    it_id = int(request.POST.get('item_id'))
    it_ob = get_object_or_404(Item, pk=it_id)

    it_info = {}
    it_info['quantity'] = int(request.POST.get('quantity'))
    it_info['price'] = float(request.POST.get('price'))
    it_info['in_date'] = request.POST.get('in_date')
    it_info['operator'] = request.POST.get('operator')

    add_items_in(it_ob, it_info)
    add_items_total(it_ob, it_info)

    dt_in = Items_in.objects.all()
    context = {}
    context['items'] = dt_in
    return render(request, 'items_in.html', context)
