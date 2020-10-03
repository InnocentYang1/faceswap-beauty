# !/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 11:11:21 2018

@author: Dawn
"""

from PIL import Image, ImageEnhance
import cv2
import numpy as np
from PIL import Image, ImageEnhance


def BrightnessEnhancement(image, brightness):
    """
    亮度增强 :brightness在（0-1）之间，新图像较原图暗，在（1-~）新图像较原图亮 ,
    brightness=1,保持原图像不变;可自定义参数范围
    """
    image_brightened = ImageEnhance.Brightness(image).enhance(brightness)

    return image_brightened


def ContrastEnhancement(image, contrast):
    """
    对比度增强: 可自定义参数contrast范围,contrast=1,保持原图像不变
    """
    image_contrasted = ImageEnhance.Contrast(image).enhance(contrast)

    return image_contrasted


def ColorEnhancement(image, color):
    """
    色度增强 : 饱和度  color=1,保持原图像不变
    """
    image_colored = ImageEnhance.Color(image).enhance(color)

    return image_colored


def SharpnessEnhancement(image, sharpness):
    """
    锐度增强: 清晰度  sharpness=1,保持原图像不变
    """
    image_sharped = ImageEnhance.Sharpness(image).enhance(sharpness)

    return image_sharped


def Filter(image, fliter):
    """
    色彩窗的半径
    图像将呈现类似于磨皮的效果

    image：输入图像，可以是Mat类型，
           图像必须是8位或浮点型单通道、三通道的图像
    """
    image = np.array(image)  # 转换为数组处理
    image_fliter = cv2.bilateralFilter(image, fliter[0], fliter[1], fliter[2])
    image_fliter = Image.fromarray(np.uint8(image_fliter)).convert('RGB')  # 转换为PIL的实例

    return image_fliter


def WhiteBeauty(image, white):
    """
    皮肤美白
    """
    image = np.array(image)  # 转换为数组处理
    image_white = np.uint8(np.clip((white * image + 10), 0, 255))
    image_white = Image.fromarray(np.uint8(image_white)).convert('RGB')  # 转换为PIL的实例

    return image_white


def beauty_face(image):
    # 设置参数
    brightness = 0.8
    contrast = 1.1
    color = 1.1
    sharpness = 1.8
    # 0：表示在过滤过程中每个像素邻域的直径范围，一般为0；后面两个数字：空间高斯函数标准差，灰度值相似性标准差。
    fliter = [0, 0, 20]
    white = 1.2

    image = Image.fromarray(np.uint8(image)).convert('RGB')

    # 对比度增强: 可自定义参数contrast范围，contrast=1，保持原图像不变
    image = ContrastEnhancement(image, contrast)

    # 色度增强: 饱和度  color=1,保持原图像不变
    image = ColorEnhancement(image, color)

    # 锐度增强: 清晰度  sharpness=1,保持原图像不变
    image = SharpnessEnhancement(image, sharpness)

    # 亮度增强 :brightness在（0-1）之间，新图像较原图暗，在（1-~）新图像较原图亮
    image = BrightnessEnhancement(image, brightness)
    # image_bright.save(result_path + '15_7_brightness.jpg')

    # 色彩窗的半径: 图像将呈现类似于磨皮的效果
    image = Filter(image, fliter)

    # 美白
    image = WhiteBeauty(image, white)

    image = np.array(image)  # 转换为数组处理

    image = cv2.bilateralFilter(image, 5, 50, 50)

    return image
