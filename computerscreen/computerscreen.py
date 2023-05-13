
import os
import pyautogui
import cv2
import numpy as np
import keyboard

# ������Ƶ������������ļ�
SCREEN_SIZE = tuple(pyautogui.size())
fourcc = cv2.VideoWriter_fourcc(*'XVID')
output_path = 'd:/python/video/abc/output.avi'
file_number = 1

# ����ļ��Ƿ���ڣ�������ھͼ�1
while os.path.exists(output_path):
    output_path = f'd:/python/video/abc/output_{file_number}.avi'
    file_number += 1


# show refresh rate
refresh_rate = pyautogui.screenshot().tobytes().__sizeof__() / (pyautogui.size().width * pyautogui.size().height * 3)

print(f"Screen refresh rate: {refresh_rate:.2f} fps")

out = cv2.VideoWriter(output_path, fourcc, 10, (SCREEN_SIZE[0]-220, SCREEN_SIZE[1]-130), isColor=True)

# ��ʼ¼��
try:
    while True:
        # ��Ļ��ͼ
        img = pyautogui.screenshot(region=(110, 90, SCREEN_SIZE[0]-220, SCREEN_SIZE[1]-130))

        # ת��Ϊ OpenCV ��ʽ
        frame = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)

        # д����Ƶ�ļ�
        out.write(frame)

        # �� Q ��ֹͣ¼��
        if keyboard.is_pressed('q'):
            break
finally:
     # �ͷ���Դ
    out.release()
    cv2.destroyAllWindows()

    # ������refresh_rate�������ٶȣ����ǲ��У�����������ÿ��10����ٶȣ�����������ԭ�ٶȲ�࣡