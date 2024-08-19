import numpy as np
import cv2
import csv
import os
import matplotlib.pyplot as plt

# 创建保存标注数据的目录
output_dir = 'annotations'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# 打开视频文件
video_path = 'E:\\_ygr\\实验\\240730激光火花试验\\200-22w.mp4'
cap = cv2.VideoCapture(video_path)
ret, image = cap.read()
roi = [869, 684, 327, 357]  # 替换为你想要的 ROI 区域
x, y, w, h = roi
image = image[y:y + h, x:x + w]

# 计算灰度直方图
hist = cv2.calcHist([image], [0], None, [256], [0, 256])
hist = hist.ravel()  # 转换为一维数组

# 计算与曲线图对应的直方图
plt.figure(figsize=(15, 5))

# 绘制灰度分布曲线图
plt.subplot(1, 2, 1)
plt.plot(hist, color="r")
plt.title("Grayscale Distribution Curve")
plt.xlabel("Gray Level")
plt.ylabel("Number of Pixels")

# 使用与曲线相同的数据绘制直方图
plt.subplot(1, 2, 2)
plt.bar(range(256), hist, color='b', width=1.0)
plt.title("Grayscale Histogram (Using the Same Data)")
plt.xlabel("Gray Level")
plt.ylabel("Number of Pixels")

# 显示图像
plt.tight_layout()
plt.show()

# 等待按键退出
cv2.waitKey(0)
cv2.destroyAllWindows()
