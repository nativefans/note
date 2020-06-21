import os

def read_path(path_name):
    print(os.listdir(path_name))
    name = 0
    for dir_item in os.listdir(path_name):
        old_path = os.path.abspath(os.path.join(path_name, dir_item))
        new_path = os.path.abspath(os.path.join(path_name,str(name)))
        os.rename(old_path,new_path)
        name+=1

if __name__ == '__main__':

    read_path('G:\\code\\study\\source_code\\LFW\\select_WebFace')