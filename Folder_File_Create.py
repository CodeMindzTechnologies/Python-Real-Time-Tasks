# Task: create a folder and create a file inside that folder 

# module - simple python file. eg: math, os, etc

import os

folder_name = "D:\\Temp"
file_name = "test.txt"

if not os.path.exists(folder_name):
    os.makedirs(folder_name)
    print("Folder created")
else:
    print("Folder already exists")

file_path = os.path.join(folder_name,file_name) 
if not os.path.exists(file_path):
    file = open(file_path,"w") # file descriptor 
    file.write("test message")
    file.close()
    print("File is created")
else:
    print("File already exists")



