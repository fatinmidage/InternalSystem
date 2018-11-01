'''处理Store的路由'''
from django.urls import path
from .views import storelist, details_in, add_items_to_intable
from .views import details_out, add_items_to_outtable
# from .views import delete_in_record, delete_out_record
# from .views import export_inventory_sheet

urlpatterns = [
    path('', storelist, name='storelist'),
    path('in/', details_in, name='details_in'),
    path('add/', add_items_to_intable, name='add_items_to_intable'),
    path('out/', details_out, name='details_out'),
    path('min/', add_items_to_outtable, name='add_items_to_outtable'),
    # path('delete_in_record/', delete_in_record, name='delete_in_record'),
    # path('delete_out_record/', delete_out_record, name='delete_out_record'),
    # path('export_excel', export_inventory_sheet, name='export_inventory_sheet'),
]
