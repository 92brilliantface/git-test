#!/usr/bin/python
import glob
import os

files = glob.glob("") #Ư��Ȯ���ڸ� ���� ��ϻ̱�
for x in files:
    if not os.path.isdir(x): 
        filename = os.path.splitext(x)
        os.rename(x, filename[0]  + '.jpg')