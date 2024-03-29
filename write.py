"""
Script to save the overlay image and the associated txt-label

The function write_obj can be used to save the overlay image to the specified
directory.
The associated label will be calculated and saved to the other stated directory
path.

Naming convention: <class-id_class-name_bounding-radius>

Functions in this module:
    *write_obj - saves the image and associated label
"""

import os
import cv2
import math


def write_obj(path, scale, variables, xC, yC, img, index):
    """
    Saves the overlay image and the associated object label

    :param path: specified image path
    :param label_path: specified label path
    :param classes: class dictionary
    :param name: class name of the current object
    :param x: x center of the bounding box
    :param y: y center of the bounding box
    :param radius: smallest enclosing radius of the bounding box
    :param img: overlay image
    :param i: counter
    :return:
    """
    if variables[0] == 'five':
        classname = 0
    elif variables[0] == 'fist':
        classname = 1

    radius = float(variables[2])
    
    width = height = 2 * radius / math.sqrt(2)
    img_height, img_width, img_ch = img.shape #rows, cols, ch

    xC1 = xC / img_width
    yC1 = yC / img_height

    rel_width = scale * width / img_width #width and height are scaled, bb cannot be left unscaled
    rel_height = scale * height / img_height
    
    text = '%d %f %f %f %f\n' % (classname, xC1, yC1, rel_width, rel_height)

    label = os.path.join(path, '%d_%d_%d_%d.txt' % (index, classname, radius, scale*100000))

    pic_path = os.path.join(path, '%d_%d_%d_%d.jpg' % (index, classname, radius, scale*100000))

    cv2.imwrite(pic_path, img)
    with open(label, 'w') as file:
        file.write(text)


