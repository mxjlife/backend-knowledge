# _*_ coding: utf8 _*_

import os
import subprocess
import fileinput
import re

base_path = os.path.dirname(os.path.realpath(__file__))

def create_file(file_path):
    path = os.path.join(base_path, file_path)
    if os.path.exists(path):
        print(file_path + ' is exist!!!')
        return False
    if not file_path.endswith('.md'):
        os.makedirs(path)
        return False
    dir_file = os.path.split(path)
    if not os.path.exists(dir_file[0]):
        os.makedirs(dir_file[0])
    file = open(path,'w')
    file.close()

#n = re.findall(r"长江学者(.+?)人", s)

#file = open('README.md')
#for line in file:
    #
#file.close()

strs = []
with open('README.md','r', encoding='utf-8') as f:
    while True:
        line = f.readline()
        if len(line) == 0:
            break;
        l = re.findall(r"\((.+?)\)", line)
        if len(l) > 0:
            strs.append(l[-1].strip())
for s in strs:
    print(s)
    create_file(s)
  