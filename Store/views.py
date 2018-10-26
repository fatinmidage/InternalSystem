"""定义处理函数"""

from django.shortcuts import render, redirect
from django.http import request
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, login
from .models import ItemsTotal, ItemsIn, Item, ItemsOut

# Create your views here.


def storelist(rq_request: request):
    """显示库存情况页面"""
    store_details = ItemsTotal.objects.all()
    context = {}
    context['store'] = store_details
    return render(rq_request, 'storelist.html', context)


def details_in(rq_request: request):
    """显示入库明细页面"""
    dt_in = ItemsIn.objects.all()
    context = {}
    context['items'] = dt_in
    return render(rq_request, 'items_in.html', context)


def add_items_in(it_object: Item, it_info: {}):
    """在数据库中添加一个入库记录"""
    it_in = ItemsIn()
    it_in.item = it_object
    it_in.quantity = it_info['quantity']
    it_in.price = it_info['price']
    it_in.total_price = it_in.quantity * it_in.price
    it_in.in_date = it_info['in_date']
    it_in.operator = it_info['operator']
    it_in.save()


def modify_items_total(it_ob: Item, num):
    """修改总表记录"""
    it_tatal = ItemsTotal
    it_tatal = get_object_or_404(ItemsTotal, item=it_ob)
    it_tatal.quantity += num
    it_tatal.save()


def add_items_to_intable(rq_request: request):
    """客户端POST提交入库"""
    it_id = int(rq_request.POST.get('item_id'))
    it_ob = get_object_or_404(Item, pk=it_id)
    it_info = {}
    it_info['quantity'] = int(rq_request.POST.get('quantity'))
    it_info['price'] = float(rq_request.POST.get('price'))
    it_info['in_date'] = rq_request.POST.get('in_date')
    it_info['operator'] = rq_request.POST.get('operator')
    add_items_in(it_ob, it_info)
    modify_items_total(it_ob, it_info['quantity'])
    dt_in = ItemsIn.objects.all()
    context = {}
    context['items'] = dt_in
    return render(rq_request, 'items_in.html', context)


def details_out(rq_request: request):
    """显示出库明细页面"""
    items_out = ItemsOut.objects.all()
    context = {}
    context['items'] = items_out
    return render(rq_request, 'items_out.html', context)


def add_items_out(it_ob, it_info):
    """在数据库中新增一条出库记录"""
    it_out = ItemsOut()
    it_out.item = it_ob
    it_out.quantity = it_info['quantity']
    it_out.out_date = it_info['out_date']
    it_out.operator = it_info['operator']
    it_out.save()


def add_items_to_outtable(rq_request: request):
    """客户端POST提交出库"""
    it_id = int(rq_request.POST.get('item_id'))
    it_ob = get_object_or_404(Item, pk=it_id)
    it_info = {}
    it_info['quantity'] = int(rq_request.POST.get('quantity'))
    it_info['out_date'] = rq_request.POST.get('out_date')
    it_info['operator'] = rq_request.POST.get('operator')
    add_items_out(it_ob, it_info)
    modify_items_total(it_ob, -it_info['quantity'])
    dt_in = ItemsOut.objects.all()
    context = {}
    context['items'] = dt_in
    return render(rq_request, 'items_out.html', context)


def log_in(rq_request: request):
    """用户登陆"""
    user_name = rq_request.POST.get('user_name')
    user_password = rq_request.POST.get('user_password')
    us_user = authenticate(
        rq_request, username=user_name, password=user_password)
    if us_user is not None:
        login(rq_request, us_user)
        return redirect('/')

    else:
        return render(rq_request, 'login_failed.html', {'message': '用户名和密码错误！'})


def log_out(rq_requesst: request):
    """用户登出"""
    pass


def delete_in_record(rq_request: request):
    """删除入库记录"""
    in_id = int(rq_request.POST.get('record_num'))
    try:
        iti_itemin = ItemsIn.objects.get(pk=in_id)
        iti_itemin.is_deleted = True
        iti_itemin.save()
        modify_items_total(iti_itemin.item, -iti_itemin.quantity)
    except:
        print(f"没有'{in_id}'这个入库单号")
    dt_in = ItemsIn.objects.all()
    context = {}
    context['items'] = dt_in
    return render(rq_request, 'items_in.html', context)


def delete_out_record(rq_request: request):
    """删除出库记录"""
    out_id = int(rq_request.POST.get('record_num'))
    try:
        ito_itemout = ItemsOut.objects.get(pk=out_id)
        ito_itemout.is_deleted = True
        ito_itemout.save()
        modify_items_total(ito_itemout.item, ito_itemout.quantity)
    except:
        print(f"没有'{out_id}'这个入库单号")
    dt_out = ItemsOut.objects.all()
    context = {}
    context['items'] = dt_out
    return render(rq_request, 'items_out.html', context)
