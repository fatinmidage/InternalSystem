"""定义处理函数"""

from django.shortcuts import render
from django.http import request
from django.shortcuts import get_object_or_404
from .models import Items_Total, Items_in, Item, Items_out

# Create your views here.


def storelist(request_rq: request):
    """docstring占位"""
    store = Items_Total.objects.all()
    context = {}
    context['store'] = store
    return render(request_rq, 'storelist.html', context)


def details_in(request_rq: request):
    """docstring占位"""
    dt_in = Items_in.objects.all()
    context = {}
    context['items'] = dt_in
    return render(request_rq, 'items_in.html', context)


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


def modify_items_total(it_ob: Item, num):
    """总表插入记录"""
    it_tatal = Items_Total
    it_tatal = get_object_or_404(Items_Total, item=it_ob)
    it_tatal.quantity += num
    it_tatal.save()


def add_items_to_intable(request_rq: request):
    """新增入库一行"""
    it_id = int(request_rq.POST.get('item_id'))
    it_ob = get_object_or_404(Item, pk=it_id)

    it_info = {}
    it_info['quantity'] = int(request_rq.POST.get('quantity'))
    it_info['price'] = float(request_rq.POST.get('price'))
    it_info['in_date'] = request_rq.POST.get('in_date')
    it_info['operator'] = request_rq.POST.get('operator')

    add_items_in(it_ob, it_info)
    modify_items_total(it_ob, it_info['quantity'])

    dt_in = Items_in.objects.all()
    context = {}
    context['items'] = dt_in
    return render(request_rq, 'items_in.html', context)


def details_out(request_rq: request):
    """docstring占位"""
    items_out = Items_out.objects.all()
    context = {}
    context['items'] = items_out
    print('测试')
    return render(request_rq, 'items_out.html', context)

def add_items_out(it_ob, it_info):
    """docstring占位"""
    it_out = Items_out()
    it_out.item = it_ob
    it_out.quantity = it_info['quantity']
    it_out.out_date = it_info['out_date']
    it_out.operator = it_info['operator']
    it_out.save()

def add_items_to_outtable(request_rq: request):
    """新增出库一行"""
    it_id = int(request_rq.POST.get('item_id'))
    it_ob = get_object_or_404(Item, pk=it_id)

    it_info = {}
    it_info['quantity'] = int(request_rq.POST.get('quantity'))
    it_info['out_date'] = request_rq.POST.get('out_date')
    it_info['operator'] = request_rq.POST.get('operator')

    add_items_out(it_ob, it_info)
    modify_items_total(it_ob, -it_info['quantity'])

    dt_in = Items_out.objects.all()
    context = {}
    context['items'] = dt_in
    return render(request_rq, 'items_out.html', context)
