from PIL import Image
import pytesseract

图片地址 = "Snipaste_2025-02-02_16-13-01.png"


def 图片识别函数(imgURL):
    # 打开图片
    img = Image.open(imgURL)

    # 增强图片对比度
    img = Image.open(imgURL).convert("L")  # 转为灰度图
    img = img.point(lambda x: 0 if x < 128 else 255)  # 二值化

    # 进行文字识别
    text = pytesseract.image_to_string(img, lang="chi_sim")

    # 打印识别结果
    print("识别结果：", text)


图片识别函数(图片地址)
