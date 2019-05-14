import pandas as pd

# t2 = pd.Series([1, 23, 1, 2, 4], index=list("abcde"))
# print(t2)

temp_dict = {"name": "Jack", "age": 23, "tel": 10086}
t3 = pd.Series(temp_dict)
print(t3)
