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
roi = [993, 816, 115, 127] # 替换为你想要的 ROI 区域
x, y, w, h = roi
image = image[y:y + h, x:x + w]

def Laplace(img, kernel):
    des_8U = cv2.filter2D(img, -1, kernel=kernel, borderType=cv2.BORDER_DEFAULT)
    des_16S = cv2.filter2D(img, ddepth=cv2.CV_16SC1, kernel=kernel, borderType=cv2.BORDER_DEFAULT)

    g = img - des_16S
    g[g < 0] = 0
    g[g > 255] = 255

    plt.figure(figsize=(10, 14))

    # origin, des_8U, des_16S, filtered
    plt.subplot(221)
    plt.imshow(img, cmap='gray')
    plt.title('origin')

    plt.subplot(222)
    plt.imshow(des_8U, cmap='gray')
    plt.title('des-8U')

    plt.subplot(223)
    plt.imshow(des_16S, cmap='gray')
    plt.title('des-16S')

    plt.subplot(224)
    plt.imshow(g, cmap='gray')
    plt.title('g')
    plt.show()




f = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

kernel1 = np.asarray([[0, 1, 0],
                      [1, -4, 1],
                      [0, 1, 0]])

Laplace(f, kernel1)

kernel2 = np.asarray([[1, 1, 1],
                      [1, -8, 1],
                      [1, 1, 1]])

Laplace(f, kernel2)

