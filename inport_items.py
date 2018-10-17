# 读取物品类型
import pandas as pd

df = pd.DataFrame()

df = pd.read_excel('C:/Users/fg104/Desktop/汇总.xlsx',
                   sheet_name='库存总表', index_col='序号')


# print(df.shape)
# print(df.columns)
# print(df.head())
print(df['位置'][25])
