import pandas as pd

df = pd.read_csv("./dogNames2.csv")
# print(df.head())
# print(df.info())

# DataFrame中排序的方法
df = df.sort_values(by='Count_AnimalName', ascending=False)
# 对行进行操作
# print(df[:20])
# # 对列进行操作
# print(df["Row_Labels"])
# print(type(df["Row_Labels"]))

print(df[(500 < df['Count_AnimalName']) & (df['Count_AnimalName'] < 900)])
