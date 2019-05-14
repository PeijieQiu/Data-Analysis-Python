import pandas as pd
import numpy as np

file_path = "./starbucks_store_worldwide.csv"
df = pd.read_csv(file_path)
# print(df.head(1))
print(df.info())

grouped = df.groupby(by="Country")
# print(grouped)

# DataFrameGroupBy

# 可以遍历
# for i in grouped:
#     print("*" * 100)
#     print(i)
# df[df["Country"] = "US"]

# 使用聚合方法
# country_count = grouped["Brand"].count()
# print(country_count["US"])
# print(country_count["CN"])

# 统计中国每个省份的店铺的数量
# China_data = df[df["Country"] == "CN"]
#
# grouped = China_data.groupby(by="State/Province").count()["Brand"]
# print(grouped)

# 数据按照多个条件进行分组, 返回Series
# grouped = df["Brand"].groupby(by=[df["Country"], df["State/Province"]]).count()
# print(grouped)

# 数据按照多个条件进行分组, 返回DataFrame
grouped = df[["Brand"]].groupby(by=[df["Country"], df["State/Province"]]).count()
# print(grouped)

# 索引的方法和属性
print(grouped.index)
