import numpy as np
import cv2
import csv
import os
import matplotlib.pyplot as plt

C = 1000

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


# 绘制对数变换曲线
def log_plot(c):
    x = np.arange(0, 256, 0.01)
    y = c * np.log(1 + x)
    plt.plot(x, y, 'r', linewidth=1)
    # 正常显示中文标签
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.title(u'对数变换函数')
    plt.xlabel('灰度值')
    plt.ylabel('变换后灰度值')
    plt.xlim(0, 255)
    plt.ylim(0, 255)
    plt.grid(True)
    plt.show()


# 对数变换
def log_transform(c, image):
    # 确保输入为浮点型并避免对数中的零问题
    img_float = image.astype(np.float32)
    img_float += 1  # 避免对数中的零
    output = c * np.log(img_float)
    # 归一化到[0,255]并转换为8位图像
   # output = cv2.normalize(output, None, 0, 255, cv2.NORM_MINMAX)
    output = np.uint8(output)
    return output



# 检查图像是否正确读取
if image is None:
    raise ValueError("图像读取失败，请检查文件路径。")

# 将图像转换为灰度图像
gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


# 绘制对数变换曲线
log_plot(C)

# 图像灰度对数变换
result = log_transform(C, gray_img)

# 显示图像
cv2.imshow("Original Image", gray_img)
cv2.imshow("Log Transformed Image", result)

# 等待显示
cv2.waitKey(0)
cv2.destroyAllWindows()