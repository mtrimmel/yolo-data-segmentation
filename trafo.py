# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 22:26:39 2020

@author: Hansi
"""
import cv2
import numpy as np


def geometric_transformation(img, angle, scale, x, y):
    rows, cols, ch = img.shape  # gets the shape of the image

    M = cv2.getRotationMatrix2D((x, y), angle, 1)  # last factor determines size of output img being rotated
    rotated_img = cv2.warpAffine(img, M, (cols, rows))  # cols,rows determine size of output window
    rotated_img = cv2.resize(rotated_img, None, fx=scale, fy=scale, interpolation=cv2.INTER_AREA)

    # cv2.imwrite('img_rotated.png', rotated_img)
    return rotated_img
