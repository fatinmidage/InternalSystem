"""导入excel表"""
import pandas as pd
from Store.models import Item


data_frame = pd.DataFrame()
data_frame = pd.read_excel('汇总.xlsx',
                   sheet_name='库存总表', index_col='序号')
it_item = Item()
print(it_item)
print(data_frame['物品'][25])
