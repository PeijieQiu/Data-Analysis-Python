import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

file_path = "./911.csv"
df = pd.read_csv(file_path)
# print(df.head(1))
# print(df.info())

# 获取分类
temp_list = df["title"].str.split(":").tolist()
cate_list = [i[0] for i in temp_list]
cate_df = pd.DataFrame(np.array(cate_list).reshape((df.shape[0], 1)))
df["cate"] = cate_df

print(df.groupby(by="cate").count()["title"])
