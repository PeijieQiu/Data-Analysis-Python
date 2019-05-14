import matplotlib.pyplot as plt
import random
from matplotlib import font_manager

my_font = font_manager.FontProperties(fname="C://Windows/Fonts/msjh.ttc")


x = range(0, 120)
y = [random.randint(20, 35) for i in range(120)]

fig = plt.figure(figsize=(20, 8), dpi=80)

plt.plot(x, y)

# 调整x轴的刻度
_x = list(x)
_xtick_labels = ["10点{}分".format(i) for i in range(60)]
_xtick_labels += ["11点{}分".format(i) for i in range(60)]
plt.xticks(_x[::3], _xtick_labels[::3], rotation=45, fontproperties=my_font)

# 添加描述信息
plt.xlabel("时间", fontproperties=my_font)
plt.ylabel("温度 单位(℃)", fontproperties=my_font)
plt.title("10点到12点每分钟的气温变化情况", fontproperties=my_font)

plt.savefig('./天气预报.png')
plt.show()
