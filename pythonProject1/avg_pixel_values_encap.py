import numpy as np
import cv2
import os
import matplotlib.pyplot as plt


def process_video(video_path, roi):
    # 打开视频文件
    cap = cv2.VideoCapture(video_path)

    # 定义 ROI 区域
    x, y, w, h = roi

    avg_pixel_values = []  # 用于储存每一帧的平均像素值

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

    return avg_pixel_values


def plot_comparison(video_data):
    for label, avg_pixel_values in video_data.items():
        plt.plot(avg_pixel_values, label=label)

    plt.xlabel('Frame Number')
    plt.ylabel('Average Pixel Value')
    plt.title('Average Pixel Value per Frame for Multiple Videos')
    plt.legend()
    plt.show()


# 设置视频路径和 ROI 区域
video_paths = {
    'Video 1': 'E:\\_ygr\\实验\\240730激光火花试验\\200-22w.mp4',
    'Video 2': 'E:\\_ygr\\实验\\240730激光火花试验\\300-30w.mp4',
    'Video 3': 'E:\\_ygr\\实验\\240730激光火花试验\\400-45w.mp4',
    'Video 4': 'E:\\_ygr\\实验\\240730激光火花试验\\500-60w.mp4'
}

roi = [993, 816, 115, 127]  # 替换为你想要的 ROI 区域

# 处理多个视频并储存结果
video_data = {}
for label, video_path in video_paths.items():
    avg_pixel_values = process_video(video_path, roi)
    video_data[label] = avg_pixel_values

# 绘制对比图
plot_comparison(video_data)
