import os
import pyautogui
import cv2
import numpy as np
import keyboard

# 设置视频编码器和输出文件
SCREEN_SIZE = tuple(pyautogui.size())
fourcc = cv2.VideoWriter_fourcc(*'XVID')
output_path = 'd:/python/video/abc/output.avi'
file_number = 1

# 检查文件是否存在，如果存在就加1
while os.path.exists(output_path):
    output_path = f'd:/python/video/abc/output_{file_number}.avi'
    file_number += 1

import pyautogui

# show refresh rate
refresh_rate = pyautogui.screenshot().tobytes().__sizeof__() / (pyautogui.size().width * pyautogui.size().height * 3)

print(f"Screen refresh rate: {refresh_rate:.2f} fps")

out = cv2.VideoWriter(output_path, fourcc, 10, (SCREEN_SIZE[0]-520, SCREEN_SIZE[1]-150), isColor=True)

# 开始录制
try:
    while True:
        # 屏幕截图
        img = pyautogui.screenshot(region=(370, 110, SCREEN_SIZE[0]-520, SCREEN_SIZE[1]-150))

        # 转换为 OpenCV 格式
        frame = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)

        # 写入视频文件
        out.write(frame)

        # 按 Q 键停止录制
        if keyboard.is_pressed('q'):
            break
finally:
     # 释放资源
    out.release()
    cv2.destroyAllWindows()

    # 本想用refresh_rate来控制速度，但是不行，我这里用了每秒10贞的速度，好像看起来跟原速度差不多！



