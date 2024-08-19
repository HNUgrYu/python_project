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

roi = [993, 816, 115, 127] # 替换为你想要的 ROI 区域
x, y, w, h = roi


# 定义全局变量
avg_pixel_values=[]  # 用于储存每一帧的平均像素值


# 遍历视频中的每一帧
while cap.isOpened():
    ret, image = cap.read()

    if not ret:
        break


    image = image[y:y + h, x:x + w]

    # 转换为灰度图像
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 计算平均像素值
    avg_pixel_value = np.mean(gray)
    avg_pixel_values.append(avg_pixel_value)

# 释放视频捕获对象
cap.release()

# 绘制平均像素值变化趋势图
plt.plot(avg_pixel_values)
plt.xlabel('Frame Number')
plt.ylabel('Average Pixel Value')
plt.title('Average Pixel Value per Frame')
plt.show()