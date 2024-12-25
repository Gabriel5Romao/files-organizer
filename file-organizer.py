import os
import sys


to_ignore_ext=["py","rar","7z","zip","deb"]

def get_all_files():
    return os.listdir(get_current_directory())

def get_current_directory():
    return os.getcwd()

def make_dir(name):
    os.mkdir(name)
    
def get_extension(file):
    return file.split(".")[-1]
    
files = get_all_files()

for file in files:
    if get_extension(file) in to_ignore_ext:
        continue
    if os.path.isfile(file):
        ext = get_extension(file)
        if not os.path.exists(ext.upper()):
            make_dir(ext.upper())
        os.rename(file,ext.upper()+"/"+file)
