# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 22:26:39 2020

@author: Hansi
"""
import cv2
import numpy as np



def geometric_transformation(img, angle, scale, x, y):
    
    
    rows, cols, ch = img.shape #gets the shape of the image
    
    M= cv2.getRotationMatrix2D((x,y), angle, scale) #last factor determines size of output img being rotated
    rotated_img = cv2.warpAffine(img, M, (rows,cols)) #cols,rows determine soze of output window 


    cv2.imwrite('img_rotated.png', rotated_img)
    return rotated_img