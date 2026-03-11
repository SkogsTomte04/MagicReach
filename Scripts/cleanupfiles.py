### script based on tutorial from w3schools url: https://www.geeksforgeeks.org/python/rename-all-file-names-in-your-directory-using-python/
# This script renames all files in a directory to a 4 digit padded filename iterating from the last: frame_0001, frame_0002, frame_0003...

import os

os.chdir('D:\\Users\\270331790\\OneDrive - UP Education\\Documents\\MagicProgress\\Environment\\MTG- Card Detecton.v2i.yolov8\\parse_env\\images')
print(os.getcwd())

for count, f in enumerate(os.listdir()):
    f_name, f_ext = os.path.splitext(f)
    f_name = "frame_" + f"{count+1:04d}"

    new_name = f'{f_name}{f_ext}'
    os.rename(f, new_name)
