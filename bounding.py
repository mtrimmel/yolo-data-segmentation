"""
Script to find the center (x,y) and radius values from a bounding box

The function find_boundaries can be used to search for the circle bounding
box with the smallest enclosing circle. It then returns the center and radius
of it.

Functions in this module:
    *find_bounding - finds the smallest bounding box with center and radius
"""

import cv2


def find_bounding(img):
    """
    Finds the smallest circle bounding box of a picture

    :param img: picture for searching the bounding box
    :return: bounding box center (x,y) and radius
    """
    # Finding the contour of the object
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY)
    ret, thresh = cv2.threshold(gray_img, 127, 255, 0)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL,
                                           cv2.CHAIN_APPROX_SIMPLE)
    cnt = contours[0]

    # Finding the bounding circle
    ((x, y), radius) = cv2.minEnclosingCircle(cnt)

    return x, y, radius


    """
    #find contours of rotated image
    copy = cv2.cvtColor(rotated_img, cv2.COLOR_BGRA2GRAY)
    thresh = cv2.adaptiveThreshold(copy,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                   cv2.THRESH_BINARY,11,2)
    contours,hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, 
                                          cv2.CHAIN_APPROX_SIMPLE)
    cnt = contours[0] 

    #Bounding rectangle
    x,y,w,h = cv2.boundingRect(cnt)
    rect = cv2.minAreaRect(cnt)
    box = cv2.boxPoints(rect)
    box = np.int0(box)
    cv2.drawContours(rotated_img,[box],0,(0,0,255),2)
    cv2.rectangle(rotated_img,(x,y),(x+w,y+h),(0,255,0),2)

    #Bounding circle
    ((a, b), radius) = cv2.minEnclosingCircle(cnt)
    cv2.circle(rotated_img, (int(a), int(b)), int(radius),(0, 255, 255), 2)  
    """