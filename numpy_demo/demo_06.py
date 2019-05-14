import numpy as np
from matplotlib import pyplot as plt

us_file_path = "./youtube_video_data/US_video_data_numbers.csv"
uk_file_path = "./youtube_video_data/GB_video_data_numbers.csv"

# 加载国家数据
us_data = np.loadtxt(us_file_path, delimiter=",", dtype="int")
uk_data = np.loadtxt(uk_file_path, delimiter=",", dtype="int")

# 取评论数据
t_us_comments = us_data[:, -1]
# 选择比5000小的数据
t_us_comments = t_us_comments[t_us_comments <= 5000]

print(t_us_comments.max(), t_us_comments.min())

d = 185

bin_nums = (t_us_comments.max() - t_us_comments.min()) // d

plt.figure(figsize=(20, 8), dpi=80)

plt.hist(t_us_comments, bin_nums)

# 设置x轴刻度
plt.xticks(range(min(t_us_comments), max(t_us_comments)+d, d))

plt.grid()

plt.show()
