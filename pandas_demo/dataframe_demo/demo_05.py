import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

file_path = './IMDB-Movie-Data.csv'

df = pd.read_csv(file_path)
# print(df.head(1))
# print(df.info())

# 统计分类的列表
temp_list = df['Genre'].str.split(',').tolist()
genre_list = list(set([i for j in temp_list for i in j]))

# 构造全为0的数组
zero_df = pd.DataFrame(np.zeros((df.shape[0], len(genre_list))), columns=genre_list)
# print(zero_df)

# 给每个位置出现分类的位置赋值为1
for i in range(df.shape[0]):
    zero_df.loc[i, temp_list[i]] = 1

# 统计每个分类的电影的数量和
genre_count = zero_df.sum(axis=0)
# print(genre_count)

# 排序
genre_count = genre_count.sort_values()
_x = genre_count.index
_y = genre_count.values
print(type(genre_count))

# 画图
plt.figure(figsize=(20, 8), dpi=100)
plt.bar(range(len(_x)), _y)
plt.xticks(range(len(_x)), _x)
plt.show()
