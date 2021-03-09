import glob
import os


def process_images(percentage_test, path):

    # directory where the data will reside, relative to 'darknet.exe'
    path_data = os.path.join(path, 'generated_images')
    dir_path = '/home/lv71515/MTrimmel/darknet/build/darknet/x64/data/obj/'


    # create and/or truncate train.txt and test.txt
    file_train = open('train_1.txt', 'w')
    file_test = open('test_1.txt', 'w')

    # fill the files train.txt and test.txt
    counter = 1
    index_test = round(100 / percentage_test)
    for pathAndFilename in glob.iglob(os.path.join(path_data, "*.jpg")):
        title, ext = os.path.splitext(os.path.basename(pathAndFilename))
        if counter == index_test:
            counter = 1
            file_test.write(dir_path + title + '.jpg' + '\n')
        else:
            file_train.write(dir_path + title + '.jpg' + '\n')
            counter = counter + 1
