import pandas as pd
from matplotlib import pyplot as plt

file_path = './IMDB-Movie-Data.csv'

df = pd.read_csv(file_path)
# print(df.head(1))
# print(df.info())

# rating runtime的分布情况
# 直方图
# 准备数据
runtime_data = df["Runtime (Minutes)"].values
max_runtime = runtime_data.max()
min_runtime = runtime_data.min()
print(max_runtime - min_runtime)
d = 5
num_bin = (max_runtime - min_runtime) // d

plt.figure(figsize=(20, 8), dpi=80)
plt.hist(runtime_data, num_bin)

plt.xticks(range(min_runtime, max_runtime+5, 5))

plt.grid()

plt.show()
