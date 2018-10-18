'''处理Store的路由'''
from django.urls import path
from .views import storelist, details_in, add_items_to_intable

urlpatterns = [
    path('', storelist, name='storelist'),
    path('in/', details_in, name='details_in'),
    path('add/', add_items_to_intable, name='add_items_to_intable'),
]