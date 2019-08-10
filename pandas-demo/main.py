import pandas as pd
import numpy as np

# 从 csv 文件读数据
data = pd.DataFrame(pd.read_csv('pandas-datasets.csv'))

# 删除空白值大于等于3个的行，直接在原数据集上操作。
data.dropna(axis=0, thresh=3, inplace=True)
# 重置索引 
data.reset_index(drop=False, inplace=True)

# 填充空白值，hour 列的空白值填充为 9，将 temperature 列的空白值填充为 25.5
data.fillna({ 'hour': 10, 'temperature': 25.5 }, inplace=True)

# 索引最大值 13。总共有 14 个数，索引是 0-13
num = data.index.max() 
# 循环数组，拿到每一行的 hour 字段值，与 24 做比较，大于 24，删除改行     
for i in range(num):
    if data.loc[i, 'hour'] > 24:
        data.drop([i], inplace=True)
# 删除行后索引值会改变，记得重置索引值
data.reset_index(drop=False, inplace=True)

# 删除 pandas 自动生成的两列 'level_0', 'index'
data.drop(axis=1, columns=['level_0', 'index'], inplace=True)
# 删除重复值，只保留第一次出现的值
data.drop_duplicates(keep='first', inplace=True)
# 删除行后索引值会改变，记得重置索引值
data.reset_index(drop=False, inplace=True)

# 生成个随机数数组
random = np.random.permutation(data.index.size)
# 数据重排，打乱顺序
data2 = data.take(random)

# 随机取 8 条数据
data3 = data2.sample(8)

print(data3)
