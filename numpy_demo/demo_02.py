import numpy as np

us_file_path = "./youtube_video_data/US_video_data_numbers.csv"
uk_file_path = "./youtube_video_data/GB_video_data_numbers.csv"

# t1 = np.loadtxt(us_file_path, delimiter=",", dtype="int", unpack=True)
t2 = np.loadtxt(us_file_path, delimiter=",", dtype="int")

# print(t1)
# print("*"*100)
print(t2)
print("*" * 100)

# 取行
# print(t2[2])

# 取连续多行
# print(t2[2:])

# 取不连续多行
# print(t2[[2, 4, 8]])

# 取列
# print(t2[1, :])
# print(t2[2:, :])
# print(t2[[2, 4, 8], :])
# print(t2[:, 0])
# print(t2[:, 2:])

# 取第3行，第4列数据
# print(t2[2, 3])

# 取第3-5行，第2-4列数据
# b = t2[2:5, 1:4]
# print(b)

# 取多个不相邻的点
c = t2[[0, 2, 2], [0, 1, 3]]
print(c)
