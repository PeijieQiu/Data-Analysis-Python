from typing import List

import matplotlib.pyplot as plt


x = range(2, 26, 2)
y = [15, 13, 14.5, 17, 20, 25, 26, 26, 27, 22, 18, 15]
fig = plt.figure(figsize=(20, 8), dpi=80)
plt.plot(x, y)

# 设置x轴的刻度
_xtick_labels = [i/2 for i in range(4, 49)]
plt.xticks(_xtick_labels[::3])
plt.yticks(range(min(y), max(y)+1))

# plt.savefig("./sig_size.png")
plt.show()

