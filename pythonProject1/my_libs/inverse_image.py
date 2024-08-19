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

def inverse_image(img):
    rows,cols=img.shape[:2]
    for i in range(rows):
        for j in range(cols):
            img[i,j]=255 - img[i,j]

    return img


cv2.namedWindow('Original Image', 0)
cv2.resizeWindow('Original Image', 500, 500)  # 设置窗口大小
cv2.imshow('Original Image', inverse_image(gray))

# 等待按键退出
cv2.waitKey(0)
cv2.destroyAllWindows()


