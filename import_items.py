"""导入excel表，需要提前安装pandas和lxrd"""
import pandas as pd
from Store.models import Item, ItemsTotal


df_dataframe = pd.DataFrame()
df_dataframe = pd.read_excel('汇总.xlsx',
                             sheet_name='库存总表', index_col='序号')
for i in range(1, len(df_dataframe)+1):
    it = Item()
    it.name = df_dataframe['物品'][i]
    it.item_model = df_dataframe['规格型号'][i]
    it.unit = df_dataframe['单位'][i]
    it.location = df_dataframe['位置'][i]
    it.save()

for i in range(len(df_dataframe)):
    its = ItemsTotal()
    its.item = Item.objects.all()[i]
    its.quantity = df_dataframe['结余'][i+1]
    its.save()
    print(its.item.name)

def export_inventory_sheet(rq_request:request):
    """导出盘点表"""
    # 1.对总表的位置列去重并排序，得到一个唯一有序的“位置数组”
    # 2.遍历“位置数组”，通过fileter函数查询同一位置的queryset，并添加到新的对象中
    # 3.删除对象中数量为零的行
    # 4.保存整理结果到excel文件