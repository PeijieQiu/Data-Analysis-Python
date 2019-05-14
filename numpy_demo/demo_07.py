import numpy as np
from matplotlib import pyplot as plt

us_file_path = "./youtube_video_data/US_video_data_numbers.csv"
uk_file_path = "./youtube_video_data/GB_video_data_numbers.csv"

# 加载国家数据
uk_data = np.loadtxt(uk_file_path, delimiter=",", dtype="int")
uk_data = uk_data[uk_data[:, 1] <= 50000]

t_uk_comments = uk_data[:, -1]
t_uk_like = uk_data[:, 1]

plt.figure(figsize=(20, 8), dpi=80)

plt.scatter(t_uk_like, t_uk_comments)

plt.show()
