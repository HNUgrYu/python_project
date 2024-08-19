import cv2
import numpy as np
import csv
import os


# 创建保存标注数据的目录
output_dir = 'annotations'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# 打开视频文件
video_path = 'E:\\_ygr\\实验\\240730激光火花试验\\500-60w.mp4'
cap = cv2.VideoCapture(video_path)

# 定义全局变量
point_list = []  # 用于存储手动标注的点
frame_count = 0  # 帧计数
previous_point = None  # 用于存储前一帧火花的位置
velocity_list = []  # 用于存储速度数据
angle_list = []  # 用于存储角度数据
avg_pixel_values=[]  # 用于储存每一帧的平均像素值

# 鼠标点击事件回调函数，用于标注火花的位置
def click_event(event, x, y, flags, param):
    global point_list
    if event == cv2.EVENT_LBUTTONDOWN:
        point_list.append((x, y))

# 计算两个点之间的距离（速度）
def calculate_distance(point1, point2):
    return np.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)

# 计算两个点之间的角度
def calculate_angle(point1, point2):
    return np.degrees(np.arctan2(point2[1] - point1[1], point2[0] - point1[0]))

# 创建CSV文件并写入标题行
with open(os.path.join(output_dir, 'annotations.csv'), mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Frame', 'Point_X', 'Point_Y', 'Velocity', 'Angle', 'Color_Hue'])

# 定义 ROI 区域 (x, y, width, height)
roi = [869, 684, 327, 357]  # 替换为你想要的 ROI 区域

# 逐帧读取视频
while True:
    ret, frame = cap.read()
    if not ret:
        break


    # 从 ROI 信息中提取 x, y, width, height
    x, y, w, h = roi

    # 提取 ROI 区域
    frame = frame[y:y + h, x:x + w]

    # 显示当前帧
    cv2.imshow('Video', frame)

    # 绑定鼠标事件
    cv2.setMouseCallback('Video', click_event)

    # 等待用户按下 'n' 键来标注下一帧
    key = cv2.waitKey(0) & 0xFF
    if key == ord('n'):
        # 标注当前帧的所有点
        for point in point_list:
            cv2.circle(frame, point, 5, (0, 0, 255), -1)  # 用红色圆圈标注火花

            # 计算速度和角度
            if previous_point is not None:
                velocity = calculate_distance(previous_point, point)
                angle = calculate_angle(previous_point, point)
            else:
                velocity = 0
                angle = 0

            velocity_list.append(velocity)
            angle_list.append(angle)

            # 提取颜色（这里我们使用HSV色彩空间的色调值来表示颜色）
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            hue = hsv[point[1], point[0], 0]

            # 将数据写入CSV文件
            with open(os.path.join(output_dir, 'annotations.csv'), mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([frame_count, point[0], point[1], velocity, angle, hue])

            # 更新前一帧的点
            previous_point = point

        # 清空点列表，准备标注下一帧
        point_list.clear()

        # 增加帧计数
        frame_count += 1

    elif key == ord('q'):  # 按 'q' 键退出标注
        break

# 释放视频资源并关闭窗口
cap.release()
cv2.destroyAllWindows()

# 打印输出的标注数据路径
print(f"Annotations saved to {output_dir}")
