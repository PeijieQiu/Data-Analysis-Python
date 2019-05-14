import pandas as pd
import numpy as np

# t1 = pd.DataFrame(np.arange(12).reshape(3, 4), index=list("abc"), columns=list("WXYZ"))
# print(t1)

# d1 = {"name": ["Jack", "ABigale"], "age": [28, 32], "tel": [10086, 10000]}
# t2 = pd.DataFrame(d1)
# print(t2)

d2 = [{"name": "Jack", "age": 23, "tel": 10086}, {"name": "Abigale", "tel": 10000},
      {"name": "Scott", "age": 22}]
t3 = pd.DataFrame(d2)
print(t3)


