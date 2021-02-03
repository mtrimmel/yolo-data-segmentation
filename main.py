# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 14:46:15 2021

@author: Hansi

loading of dirs and applying trafo and alpha to background and foreground img.
"""
import cv2
import random
import os
import math
from alpha3 import alpha
from trafo import geometric_transformation
import read_names as classes
from bounding import find_bounding
from write import write_obj

# Amount of files
count = 10  # determines the number of generate images from each template and corresponding background

# Paths for pictures and .txt-files
dir_path = os.path.dirname(os.path.realpath(__file__))  # path to current directory
path = os.path.join(dir_path, 'generated_images')  # dir path for generated images
img_dir = os.path.join(dir_path, 'templates')  # path for template images
background_dir = os.path.join(dir_path, 'backgrounds')  # separate folder for background images

# Classes from the obj.txt file
classes = classes.read_classes()

for background in os.listdir(background_dir):
    background_path = os.path.join(background_dir, '{}'.format(background))
    for obj in os.listdir(img_dir):

        # call name of the image
        name = '{}'.format(obj)
        # split name
        # 0: class
        # 1: MOD
        # 2: Radius
        # 3: x coordinate
        # 4: y coordinate
        # 5: image index number
        variables = name.split('_')
        MOD = float(variables[1])  # minimum object distance
        print(variables)
        image_path = os.path.join(img_dir, '{}'.format(name))
        for i in range(count):
            # Get foreground and background
            img1 = cv2.imread(image_path, -1)  # template image
            img2 = cv2.imread(background_path)  # background image

            # Rotation angle for geometric transformation
            rotation_angle = random.randrange(0, 360, 1)

            # Scaling of img1 using similar triangles
            z_in = MOD
            z_out = random.uniform(3.0,4.0)
            scale = z_in / z_out
            # print(x_in, 1/x_out)

            rotated_img = geometric_transformation(img1, rotation_angle, scale, float(variables[3]),
                                                   float(variables[4]))

            x_offset = random.randrange(1, img2.shape[1] - rotated_img.shape[1],
                                        1)
            y_offset = random.randrange(1, img2.shape[0] - rotated_img.shape[0],
                                        1)

            # Overlaying the object to the background and transparent image
            contour_img, overlay = alpha(rotated_img, img2, x_offset, y_offset)

            # Optional - draw bounding rectangle and circle
            radius = scale * float(variables[2])
            radius = int(radius)
            x_center = float(variables[3])
            x_center = int(x_center)
            y_center = float(variables[4])
            y_center = int(y_center)
            x_rect1 = x_offset + x_center - radius
            y_rect1 = y_offset + y_center - radius
            x_rect2 = x_offset + x_center + radius
            y_rect2 = y_offset + y_center + radius
            xC = x_offset + x_center
            yC = y_offset + y_center
            # print(radius, x_center, y_center, x_rect1, y_rect1)
            # cv2.circle(overlay,(x_offset+x_center,y_offset+y_center),3,(0,255,0),3)
            cv2.rectangle(overlay, (x_rect1, y_rect1),
                          (x_rect2, y_rect2), (255, 0, 0), 1)

            # Saving the picture and writing the corresponding .txt-file
            write_obj(path, path, variables, xC, yC, overlay, i)
