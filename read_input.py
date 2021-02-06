"""

"""

import os
import glob
import re
import pathlib


def get_img():
    """

    :return:
    """

    types = ('*.png', '*.jpg', '*.jpeg')

    current_dir_file = os.path.dirname(os.path.abspath(__file__))
    backgrounds = []
    for type in types:
        background_searchpath = os.path.join(current_dir_file, 'input',
                                              'background', type)
        backgrounds.extend([img for img in glob.glob(background_searchpath)])
    backgrounds.sort()

    template_searchpath = os.path.join(current_dir_file, 'input', 'template',
                                       '*.png')
    templates = sorted([img for img in glob.glob(template_searchpath)])

    return backgrounds, templates

def get_yolo_obj():

    current_dir_file = os.path.dirname(os.path.abspath(__file__))

    object_searchpath= os.path.join(current_dir_file, 'input', 'yolo_objects')
    obj_data = glob.glob(os.path.join(object_searchpath, '*.data'))
    obj_names = glob.glob(os.path.join(object_searchpath, '*.names'))

    return obj_data[0], obj_names[0]

def read_yolo_data(obj_file):

    obj_data = []
    with open(obj_file, 'r') as obj_input:
        for line in obj_input:
            obj_data.append(line)

    obj_classes_search = re.search('classes\s*=\s*(\d+)', obj_data[0])
    obj_classes = str(obj_classes_search.group(1))

    obj_train_line = pathlib.Path(obj_data[1])
    obj_train_search = re.search('train\s*=\s*(.+)', str(obj_train_line.parent))
    obj_train_path = str(obj_train_search.group(1))
    obj_train = (obj_train_path, obj_train_line.name)

    obj_valid_line = pathlib.Path(obj_data[2])
    obj_valid_search = re.search('valid\s*=\s*(.+)', str(obj_valid_line.parent))
    obj_valid_path = str(obj_valid_search.group(1))
    obj_valid = (obj_valid_path, obj_valid_line.name)

    obj_names_line = pathlib.Path(obj_data[3])
    obj_names_search = re.search('names\s*=\s*(.+)', str(obj_names_line.parent))
    obj_names_path = str(obj_names_search.group(1))
    obj_names = (obj_names_path, obj_names_line.name)

    return obj_classes, obj_train, obj_valid, obj_names

def read_yolo_classes(obj_file):
    """
    Generating a list of .txt files from the working directory

    Keyword arguments:
    :param obj_file: searched file (default 'obj.txt')
    :return: dictonary containing object names and class-id
    """
    names = []
    class_id = []
    class_n = 0

    with open(obj_file, 'r') as obj_input:
        for line in obj_input:
            names.append(line.rstrip())
            class_id.append(class_n)
            class_n = class_n + 1

    obj_class_dict = dict(zip(names, class_id))

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

    print('obj_data - classes:')
    print(*obj_data_classes)
    print('obj_data - train:')
    print(*obj_data_train)
    print('obj_data - valid:')
    print(*obj_data_valid)
    print('obj_data - names:')
    print(*obj_data_names)