import os

os.chdir('/mnt/4EA8C0A3A8C08AC3/MegaSync/python-folder/File names changer/example')

for i in os.listdir():
    f_name,f_ext=i.split(".")
    f_name_new = f_name.split("- ")[1]+' - '+f_name.split(" -")[0]+"."+f_ext
    os.rename(i, f_name_new)