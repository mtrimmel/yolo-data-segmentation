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

    # Finding bounding rectangle
    rect_x, rect_y, rect_w, rect_h = cv2.boundingRect(cnt)
    cv2.rectangle(img, (rect_x, rect_y), (rect_x + rect_w, rect_y + rect_h),
                  (0, 255, 0), 2)
    rect = cv2.minAreaRect(cnt)
    box = cv2.boxPoints(rect)
    cv2.drawContours(img, [box], 0, (0, 0, 255), 2)

    # Finding bounding circle
    ((circle_x, circle_y), radius) = cv2.minEnclosingCircle(cnt)
    cv2.circle(img, (int(circle_x), int(circle_y)), int(radius),
               (0, 255, 255), 2)


def draw_bounding(img, r, x, y, scale, x_offset, y_offset):
    radius = int(scale * r)
    x_center = int(x)
    y_center = int(y)

    x_rect1 = x_offset + x_center - radius
    y_rect1 = y_offset + y_center - radius
    x_rect2 = x_offset + x_center + radius
    y_rect2 = y_offset + y_center + radius

    x_img = x_offset + x_center
    y_img = y_offset + y_center

    print(radius, x_center, y_center, x_rect1, y_rect1)
    cv2.circle(img, (x_img, y_img), 3, (0, 255, 0), 3)
    cv2.rectangle(img, (x_rect1, y_rect1), (x_rect2, y_rect2), (255, 0, 0), 1)
