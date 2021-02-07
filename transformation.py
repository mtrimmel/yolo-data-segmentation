# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 22:26:39 2020

@author: Hansi
"""
import cv2
import random


def refactor(z_in):
    # Rotation angle for geometric transformation
    rotation_angle = random.randrange(0, 360, 1)

    # Scaling of img1 using similar triangles
    z_out = random.uniform(3.0, 4.0)
    scale = z_in / z_out

    return rotation_angle, scale


def geometric_transformation(template, background, angle, scale, x, y):
    # Get shape of the image
    rows, cols, ch = template.shape

    # Last factor determines size of output img being rotated
    m = cv2.getRotationMatrix2D((x, y), angle, scale)
    # Columns and rows determine size of output window
    rotated_img = cv2.warpAffine(template, m, (rows, cols))

    x_offset = random.randrange(1,
                                background.shape[1] - rotated_img.shape[1], 1)
    y_offset = random.randrange(1,
                                background.shape[0] - rotated_img.shape[0], 1)

    return rotated_img, x_offset, y_offset


def create_overlay(foreground, background, x_offset, y_offset):
    """
    Creates overlay

    :param foreground:
    :param background:
    :param x_offset:
    :param y_offset:
    :return:
    """

    x1, x2 = x_offset, x_offset + foreground.shape[1]
    y1, y2 = y_offset, y_offset + foreground.shape[0]

    alpha = foreground[:, :, 3] / 255
    b, g, r, a = cv2.split(foreground)

    foreground = cv2.merge((b, g, r))

    # Overlaying the background with the foreground object
    for c in range(0, 3):
        background[y1:y2, x1:x2, c] = (alpha * foreground[:, :, c] +
                                       (1.0 - alpha) *
                                       background[y1:y2, x1:x2, c])

    overlay = cv2.resize(background, None, fx=1, fy=1,
                         interpolation=cv2.INTER_AREA)

    return overlay
