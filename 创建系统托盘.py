import pystray
from PIL import Image
import pyautogui
import sys

from 自动获取鼠标选择区域 import RegionSelector
from 动态识别文字 import Orcobj


selector = RegionSelector()
orc_obj = Orcobj()
def 开始识别():
    selector.root.mainloop()
    orc_obj.是否开始识别 = True
    # print(selector.MONITOR_REGION)
    orc_obj.dynamic_ocr(orc_obj,selector.MONITOR_REGION)

def 停止识别():
    orc_obj.是否开始识别 = False
    selector.cancel(selector)


def on_quit_clicked(icon):
    icon.stop()


def creat_stray():
    image = Image.open("Icon.png")
    menu = (
        pystray.MenuItem(text="开始识别", action=开始识别),
        pystray.MenuItem(text="停止识别", action=停止识别),
        pystray.MenuItem(text="退出", action=on_quit_clicked),
    )
    icon = pystray.Icon("name", image, "托盘名称", menu)
    icon.run()
