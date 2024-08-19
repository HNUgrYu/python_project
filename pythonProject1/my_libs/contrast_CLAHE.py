import numpy as np
import cv2
import csv
import os

# 创建保存标注数据的目录
output_dir = 'annotations'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# 打开视频文件
video_path = 'E:\\_ygr\\实验\\240730激光火花试验\\200-22w.mp4'
cap = cv2.VideoCapture(video_path)
ret, image = cap.read()
roi = [993, 816, 115, 127] # 替换为你想要的 ROI 区域
x, y, w, h = roi
image = image[y:y + h, x:x + w]

# 转换为灰度图像
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 创建CLAHE对象
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))

# 应用CLAHE算法（自适应直方图均衡化）——将图像像素划分为不重叠的组
clahe_result = clahe.apply(gray)

#应用直方图均衡化算法
equalizeHist_result=gray.copy()
cv2.equalizeHist(gray,equalizeHist_result)

# 显示结果
cv2.imshow('Original Image', image)
cv2.imshow('CLAHE Result', clahe_result)
cv2.imshow('equalizeHist_result', equalizeHist_result)

# 等待按键退出
cv2.waitKey(0)
cv2.destroyAllWindows()








