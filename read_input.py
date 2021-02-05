"""

"""

import os
import glob


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

def get_yolo_obj(path):

    current_dir_file = os.path.dirname(os.path.abspath(__file__))

    object_searchpath= os.path.join(current_dir_file, 'input', 'yolo_objects')
    obj_data = glob.glob(os.path.join(object_searchpath, '*.data'))
    obj_names = glob.glob(os.path.join(object_searchpath, '*.names'))

    return obj_data, obj_names

def read_yolo_obj(obj_data, obj_names):


if __name__ == "__main__":
    backgrounds, templates = get_img()
    obj_data, obj_names = get_yolo_obj()

    print('Backgorund und Templates\n')
    print(backgrounds, templates)
    print('Objects')
    print(obj_data, obj_names)