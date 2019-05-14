import pandas as pd
from matplotlib import pyplot as plt

file_path = './IMDB-Movie-Data.csv'

df = pd.read_csv(file_path)
# print(df.head(1))
# print(df.info())

# 获取平均评分
# print(df['Rating'].mean())

# 导演的人数
# print(len(set(df['Director'].tolist())))
# print(len(df['Director'].unique()))

# 演员的人数
temp_actors_list = df['Actors'].str.split(",").tolist()
print(temp_actors_list)
actors_list = [i for j in temp_actors_list for i in j]
print(actors_list)
actors_num = len(set(actors_list))
print(actors_num)
