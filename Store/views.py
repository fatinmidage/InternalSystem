from django.shortcuts import render
from django.http import request
from .models import Item,Items_Total

# Create your views here.
def storelist(request):
    store = Items_Total.objects.all()
    context = {}
    context['store'] = store
    return render(request,'storelist.html',context)