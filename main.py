# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 14:46:15 2021

@author: Hansi

loading of dirs and applying trafo and alpha to background and foreground img.
"""
import cv2
import sys
from read_input import read_mode, get_img, get_yolo_obj, read_yolo_data, \
    read_yolo_classes, read_img
from transformation import refactor, geometric_transformation, create_overlay
from bounding import draw_bounding
from write_output import write_obj
from process import process_images

# Read mode
n_img, mode = read_mode()

# Read files from input directory
backgrounds, templates = get_img()
obj_data, obj_names = get_yolo_obj()

# Read information from input files
data_classes, data_train, data_valid, data_names = read_yolo_data(obj_data)
classes = read_yolo_classes(obj_names)

# Creating images
for background in backgrounds:
    for template in templates:
        # Read image variables from name
        class_id, MOD, radius, x, y, index = read_img(template)

        for i in range(n_img):
            # Get template with alpha channel and background
            img_t = cv2.imread(template, -1)
            img_b = cv2.imread(background)

            # Rotation angle and scaling for geometric transformation
            rotation_angle, scale = refactor(MOD)

            img_rot, x_offset, y_offset = geometric_transformation(img_t, img_b,
                                               rotation_angle, scale,
                                               x, y)

            # Overlaying the object to the background and transparent image
            img_overlay = create_overlay(img_rot, img_b, x_offset, y_offset)

            # Optional - draw bounding rectangle and circle
            #draw_bounding(img_overlay, radius, x, y, scale, x_offset, y_offset)

            # Saving the picture and writing the corresponding .txt-file
           # write_obj(path, variables, xC, yC, overlay, i)

#process_images(80, dir_path)
