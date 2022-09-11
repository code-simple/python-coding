import os

s = "file.exe"

f_name = s.split('.')[0]
f_ext = s.split('.')[1]
print(f_name+'.'+f_ext)
print("FULL FILE NAME")