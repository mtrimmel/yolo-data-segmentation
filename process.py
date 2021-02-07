import glob
import os
import pathlib


def process_images(percentage_test, path):
    current_dir_file = os.path.dirname(os.path.abspath(__file__))

    # Create and/or truncate train.txt and test.txt
    file_train = open('train.txt', 'w')
    file_test = open('test.txt', 'w')

    # Fill the files train.txt and test.txt
    counter = 1
    index_test = round(100 / percentage_test)

    # Load images
    types = ('*.png', '*.jpg', '*.jpeg')
    images = []
    for type in types:
        images_search_path = os.path.join(current_dir_file,
                                             'output', 'data', type)
        images.extend(glob.glob(images_search_path))
    images.sort()

    for img in images:
        filename = pathlib.Path(img).name

        if counter == index_test:
            counter = 1
            file_test.write(path + filename + '\n')
        else:
            file_train.write(path + filename + '\n')
            counter = counter + 1