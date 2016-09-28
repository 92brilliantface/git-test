#!/usr/bin/python
import glob
import os

## 변경
files = glob.glob("E:/task/new/*") #특정확장자를 가진 목록뽑기
for x in files:
    if not os.path.isdir(x): 
        filename = os.path.splitext(x)
        os.rename(x, filename[0]  + '.jpg')