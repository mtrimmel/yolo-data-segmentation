# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 11:43:34 2020

@author: Hansi
"""
#built on https://stackoverflow.com/questions/14063070/overlay-a-smaller-image-on-a-larger-image-python-opencv

import cv2
import numpy as np


def alpha_channel(foreground, background, x_offset, y_offset):
    """
    Creates overlay

    :param foreground:
    :param background:
    :param x_offset:
    :param y_offset:
    :return:
    """
    #foreground = cv2.imread('foreground', -1)
    #background = cv2.imread('beach.jpg')
    #foreground = cv2.resize(foreground, None, fx= 0.5, fy= 0.5, interpolation=cv2.INTER_AREA)
    
    #x_offset = 2000
    #y_offset = 1000

    # Transparent picture for finding contour with same shape as background
    rows, cols, chan = background.shape
    trans_img = np.zeros((rows, cols, chan), np.uint8)
    #print(rows, cols)

    y1, y2 = y_offset, y_offset + foreground.shape[0]
    x1, x2 = x_offset, x_offset + foreground.shape[1]
    #print(x1, x2, y1, y2)
    
    alpha = foreground[:,:,3]/255
    b,g,r,a = cv2.split(foreground)

    
    foreground = cv2.merge((b,g,r))    
    
    for c in range(0,3):
        background[y1:y2, x1:x2, c] = (alpha * foreground[:, :, c] + (1.0-alpha) * background[y1:y2, x1:x2, c])

        # Overlaying the transparent background with the foreground object
        trans_img[y1:y2, x1:x2, c] = (alpha * foreground[:, :, c] + (1.0-alpha) * trans_img[y1:y2, x1:x2, c])
        
    
    background = cv2.resize(background, None, fx= 1, fy= 1, 
                            interpolation=cv2.INTER_AREA)

    # Resizing of the contour image
    trans_img = cv2.resize(trans_img, None, fx= 1, fy= 1,
                           interpolation=cv2.INTER_AREA)
    #cv2.imwrite('alpha.png', trans_img)
    
    
#    cv2.imshow('image',trans_img)
#    cv2.waitKey(0)
#    cv2.destroyAllWindows()
    return trans_img, background


