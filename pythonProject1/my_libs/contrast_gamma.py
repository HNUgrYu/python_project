import numpy as np
import cv2
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

# Gamma校正函数
def adjust_gamma(image, gamma=1.0):
    inv_gamma = 1.0 / gamma
    table = np.array([((i / 255.0) ** inv_gamma) * 255 for i in np.arange(0, 256)]).astype("uint8")
    return cv2.LUT(image, table)

# 应用Gamma校正，通常值在0.4到0.7之间较为合适
gamma_corrected = adjust_gamma(image, gamma=1.5)

# 显示结果

cv2.namedWindow('Gamma Corrected Image', 0)
cv2.resizeWindow('Gamma Corrected Image', 500, 500)  # 设置窗口大小
cv2.namedWindow('Original Image', 0)
cv2.resizeWindow('Original Image', 500, 500)  # 设置窗口大小
cv2.imshow('Original Image', image)
cv2.imshow('Gamma Corrected Image', gamma_corrected)

# 等待按键退出
cv2.waitKey(0)
cv2.destroyAllWindows()







