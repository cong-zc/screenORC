import cv2
import numpy as np
import pytesseract
import mss
import time

# 定义监控区域 (左, 上, 宽, 高)
# MONITOR_REGION = {"left": 100, "top": 200, "width": 400, "height": 200}

# OCR 配置（中英文混合识别）
TESSERACT_CONFIG = "--psm 6 -l eng+chi_sim"
from ctypes import windll


class Orcobj:
    def __init__(self):
        self.是否开始识别 = True
    # python class中的函数需要self,event参数，如果不需要可以用_代替
    def dynamic_ocr(self, _, MONITOR_REGION):
        windll.user32.SetProcessDPIAware()  # 放在代码开头
        print(f"{MONITOR_REGION},动态识别函数")
        with mss.mss() as sct:
            while self.是否开始识别:
                # 1. 截取屏幕区域
                screenshot = sct.grab(MONITOR_REGION)
                img_np = np.array(screenshot)

                # 2. 转换为 OpenCV 格式并预处理
                img = cv2.cvtColor(img_np, cv2.COLOR_BGRA2BGR)
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                # 在预处理阶段增加以下步骤
                _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)  # 二值化
                denoised = cv2.fastNlMeansDenoising(thresh, h=10)  # 降噪
                # 3. OCR 识别
                text = pytesseract.image_to_string(denoised, config=TESSERACT_CONFIG)
                print(f"识别结果: {text.strip()}")

                # 4. 按 'q' 退出循环
                if cv2.waitKey(1) & 0xFF == ord("q"):
                    break

                # 控制识别频率（例如每秒2次）
                time.sleep(0.5)
