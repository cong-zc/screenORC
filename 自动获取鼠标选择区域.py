import tkinter as tk
from tkinter import Canvas
import pyautogui

# from 动态识别文字 import dynamic_ocr

class RegionSelector:
    def __init__(self):
        self.root = tk.Tk()
        self.root.attributes("-fullscreen", True)
        self.root.attributes("-alpha", 0.3)
        self.root.attributes("-topmost", True)
        self.root.overrideredirect(True)

        self.canvas = Canvas(self.root, cursor="cross")
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.start_x = self.start_y = self.end_x = self.end_y = 0
        self.rect = None
        
        self.MONITOR_REGION = {"left": 0, "top": 0, "width": 0, "height": 0}

        # 绑定事件
        self.canvas.bind("<ButtonPress-1>", self.on_press)
        self.canvas.bind("<B1-Motion>", self.on_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_release)
        self.root.bind("<Escape>", self.cancel)  # 按ESC退出

    def on_press(self, event):
        # 记录起点并创建矩形
        self.start_x = event.x_root
        self.start_y = event.y_root
        self.rect = self.canvas.create_rectangle(
            0, 0, 0, 0, outline="#ff0000", width=2, fill="#7fff00aa"  # 半透明绿色填充
        )

    def on_drag(self, event):
        # 更新矩形终点坐标
        self.end_x = event.x_root
        self.end_y = event.y_root
        self.canvas.coords(
            self.rect, self.start_x, self.start_y, self.end_x, self.end_y
        )

    def on_release(self, event):
        # 计算标准化坐标并关闭窗口
        x1, y1 = (
            sorted((self.start_x, self.end_x))[0],
            sorted((self.start_y, self.end_y))[0],
        )
        x2, y2 = (
            sorted((self.start_x, self.end_x))[1],
            sorted((self.start_y, self.end_y))[1],
        )

        print(f"选择区域: 左上角 ({x1}, {y1}), 右下角 ({x2}, {y2})")
        print(f"区域尺寸: 宽 {x2 - x1}px, 高 {y2 - y1}px")

        
        # 截图并保存
        # screenshot = pyautogui.screenshot(region=(x1, y1, x2 - x1, y2 - y1))
        # screenshot.save("selected_region.png")
        # print("截图已保存为 selected_region.png")

        self.root.destroy()
        # 调用识别函数识别
        self.MONITOR_REGION = {"left": x1, "top": y1, "width": x2 - x1, "height": y2 - y1}
    def cancel(self, event):
        print("操作取消")
        self.root.destroy()
