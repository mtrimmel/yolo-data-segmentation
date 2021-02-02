"""
This script allows the user to search for a specific .txt-file

The function read_file can be used to search for a specific .txt-file in the
current working directory. It counts the classes and writes the class
names into a list which are then returned. Standard search is carried out for
the obj.txt file.

Functions in this module:
    *read_classes - reads the classes from a .txt-file
"""
import glob


def read_classes(obj_file='obj.txt'):
    """ 
    Generating a list of .txt files from the working directory
    
    Keyword arguments:
    :param obj_file: searched file (default 'obj.txt')
    :return: dictonary containing object names and class-id
    """
    names = []
    class_id = []
    class_n = 0

    txt_files = [f for f in glob.glob('*.txt')]

    if obj_file in txt_files:
        with open(obj_file, 'r') as f_input:
            for line in f_input:
                names.append(line.rstrip())
                class_id.append(class_n)
                class_n = class_n + 1

    obj_class_dict = dict(zip(names, class_id))

    return obj_class_dict
