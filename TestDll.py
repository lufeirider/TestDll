import shutil
import os
import re

#从info.txt提取处dll,并把dll名写入到dll.txt
with open('info.txt', 'r') as read_txt,open('dll.txt','w') as write_txt:
    dll_list = []
    text = read_txt.read()

    for i in re.findall(r"\w+\.dll", text):
        dll_list.append(i)

    dll_list = list(set(dll_list))

    for i in dll_list:
        write_txt.write(i+"\n")


#删除以前的文件夹
shutil.rmtree("test32/")
shutil.rmtree("test64/")
#新建文件夹
os.mkdir("test32/")
os.mkdir("test64/")

with open("dll.txt", "r") as f:
    while True:
        line = f.readline().strip()
        print(line)
        if line:
            shutil.copyfile("32.dll", "test32/" + line)
            copyDllFile = open("test32/" + line, "r+b")
            copyDllFile.seek(71444)  # 移动指针
            copyDllFile.write(line.encode())
            copyDllFile.close()

            shutil.copyfile("64.dll", "test64/" + line)
            copyDllFile = open("test64/" + line, "r+b")
            copyDllFile.seek(84456)  # 移动指针
            copyDllFile.write(line.encode())
            copyDllFile.close()
        else:
            break
