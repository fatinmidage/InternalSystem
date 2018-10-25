"""导入excel表"""
import pandas as pd
from Store.models import Item


data_frame = pd.DataFrame()
data_frame = pd.read_excel('汇总.xlsx',
                   sheet_name='库存总表', index_col='序号')
for i in range(len(data_frame)):
    it = Item()
    it.name = data_frame['物品'][i]
    it.item_model = data_frame['规格型号'][i]
    it.unit = data_frame['单位'][i]
    it.location = data_frame['位置'][i]
    it.save()
