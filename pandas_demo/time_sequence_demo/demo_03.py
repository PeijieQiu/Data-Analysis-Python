import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

file_path = "./911.csv"
df = pd.read_csv(file_path)

df["timeStamp"] = pd.to_datetime(df["timeStamp"])

temp_list = df["title"].str.split(":").tolist()
cate_list = [i[0] for i in temp_list]
cate_df = pd.DataFrame(np.array(cate_list).reshape((df.shape[0], 1)))
df["cate"] = cate_df
df.set_index("timeStamp", inplace=True)

plt.figure(figsize=(20, 8), dpi=80)


# 分组
for group_name, group_data in df.groupby(by="cate"):
    # 对不同的分类都进行绘图
    count_by_month = group_data.resample("M").count()["title"]
    # print(count_by_month.head(5))

    _x = count_by_month.index
    _y = count_by_month.values

    _x = [i.strftime("%Y%m%d") for i in _x]

    plt.plot(range(len(_x)), _y, label=group_name)

plt.xticks(range(len(_x)), _x, rotation=45)
plt.legend(loc="best")
plt.show()
