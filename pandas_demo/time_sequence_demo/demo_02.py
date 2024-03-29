import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

file_path = "./911.csv"
df = pd.read_csv(file_path)

df["timeStamp"] = pd.to_datetime(df["timeStamp"])
df.set_index("timeStamp", inplace=True)
# print(df.head(5))

# 统计出911中不同月份的电话次数
count_by_month = df.resample("M").count()["title"]
# print(count_by_month.head(5))

_x = count_by_month.index
_y = count_by_month.values

_x = [i.strftime("%Y%m%d") for i in _x]

plt.figure(figsize=(20, 8), dpi=80)

plt.plot(range(len(_x)), _y)

plt.xticks(range(len(_x)), _x, rotation=45)

plt.show()
