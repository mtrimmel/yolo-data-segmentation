"""
Loads files from the input directory and reads the given information

This script allows users to load files from the subdirectories of the
yolo-data-segmentation/input directory.
It loads the images from the input/background directory into a list. Images can
have a file suffix of .png, .jpg and .jpeg.
Images from the input/templates directory can have a file ending of .png and
will also be saved within a list.
The program also reads the files with .names and .data extensions from the
input/yolo_objects directory. It then generates the associated dictionary of the
class names and id from the .names file and extracts the given file path and
name of the train, valid and names part of the .data file.

The resulting information can then be displayed if the script is executed as
the main program.

This script requires that the modules 'os', 'glob', 're' and 'pathlib'
be installed within the Python environment you are running this script in.

This file can also be imported as a module and contains the following
function:
    *get_img: Generating a list of background and template images from input
              directory
    *get_yolo_obj: Get .data and .names file from input directory
    *read_yolo_data: Reads .data file per line and extracts the specified
                     information
    *read_yolo_classes: Generating a dictionary consisting of class-id and
                        associated class-name
"""

import os
import glob
import re
import pathlib


def get_img():
    """
    Generating a list of background and template images from input directory

    Background images can have a file ending of .png, .jpg and .jpeg
    Template images can have a file ending of .png

    :return: list of background images and list of template images
    """

    current_dir_file = os.path.dirname(os.path.abspath(__file__))

    # Load backgrounds
    types = ('*.png', '*.jpg', '*.jpeg')
    backgrounds = []
    for type in types:
        background_search_path = os.path.join(current_dir_file,
                                             'input', 'background', type)
        backgrounds.extend(glob.glob(background_search_path))
    backgrounds.sort()

    # Load templates
    template_search_path = os.path.join(current_dir_file,
                                       'input', 'template', '*.png')
    templates = sorted(glob.glob(template_search_path))

    return backgrounds, templates


def get_yolo_obj():
    """
    Get .data and .names file from input directory

    :return: .data and .names file
    """

    current_dir_file = os.path.dirname(os.path.abspath(__file__))

    object_search_path = os.path.join(current_dir_file, 'input', 'yolo_objects')
    obj_data = glob.glob(os.path.join(object_search_path, '*.data'))
    obj_names = glob.glob(os.path.join(object_search_path, '*.names'))

    return obj_data[0], obj_names[0]


def read_yolo_data(obj_file):
    """
    Reads .data file per line and extracts the specified information

    Extracted information consists of the number of classes and the specified
    file name and path of the train, valid and names files

    :param obj_file: YOLO object file containing specified information
    :return: number of classes and tuple of file paths and names for the train,
             valid and names file
    """

    # Generate list of lines
    obj_data = []
    with open(obj_file, 'r') as obj_input:
        for line in obj_input:
            obj_data.append(line)

    # Extract number of classes
    obj_classes_search = re.search('classes\s*=\s*(\d+)', obj_data[0])
    obj_classes = int(obj_classes_search.group(1))

    # Extract train file
    obj_train_search = re.search('train\s*=\s*(.+)', obj_data[1])
    obj_train_file = pathlib.Path(str(obj_train_search.group(1)))
    obj_train = (obj_train_file.parent, obj_train_file.name)

    # Extract valid file
    obj_valid_search = re.search('valid\s*=\s*(.+)', obj_data[2])
    obj_valid_file = pathlib.Path(str(obj_valid_search.group(1)))
    obj_valid = (obj_valid_file.parent, obj_valid_file.name)

    # Extract names file
    obj_names_search = re.search('names\s*=\s*(.+)', obj_data[3])
    obj_names_file = pathlib.Path(str(obj_names_search.group(1)))
    obj_names = (obj_names_file.parent, obj_names_file.name)

    return obj_classes, obj_train, obj_valid, obj_names


def read_yolo_classes(obj_file):
    """
    Generating a dictionary consisting of class-id and associated class-name

    Keyword arguments:
    :param obj_file: YOLO object file with names in each line
    :return: dictionary of object id and names
    """

    class_names = []
    class_id = []
    class_n = 0

    # Generate list of names and id
    with open(obj_file, 'r') as obj_input:
        for line in obj_input:
            class_names.append(line.rstrip())
            class_id.append(class_n)
            class_n = class_n + 1

    obj_class_dict = dict(zip(class_id, class_names))

    return obj_class_dict


if __name__ == "__main__":
    backgrounds, templates = get_img()
    obj_data, obj_names = get_yolo_obj()
    obj_data_classes, obj_data_train, obj_data_valid, obj_data_names = \
        read_yolo_data(obj_data)
    obj_class_dict = read_yolo_classes(obj_names)

    print('Test:')

    print('\nBackgrounds:')
    print(backgrounds)
    print('Templates:')
    print(templates)

    print('\nobj_data File:')
    print(obj_data)
    print('obj_names File:')
    print(obj_names)

    print('\nobj_data - classes:')
    print(obj_data_classes)
    print('obj_data - train:')
    print(*obj_data_train)
    print('obj_data - valid:')
    print(*obj_data_valid)
    print('obj_data - names:')
    print(*obj_data_names)

    print('\nDictionary:')
    print(obj_class_dict)
