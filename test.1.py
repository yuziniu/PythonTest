#!/usr/bin/env python
#-*- coding:utf-8 -*-
import numpy as np
import pandas as pd
from pandas import Series,DataFrame

import os
import xlrd,xlwt
def GetFileList(dir):
    filelist = []
    dir_list = os.listdir(dir)
    for i in range(0, len(dir_list)):
        path = os.path.join(dir, dir_list[i])
        if os.path.isfile(path):
           filelist.append(path)
    return filelist

xlsfile = GetFileList('d:\\test')
#xlsfile = r"D:\20180720.xlsx"
newbook = xlwt.Workbook(encoding='utf-8',style_compression=0)
newsheet = newbook.add_sheet('newsheet',cell_overwrite_ok=True)
filerow = 0
for n in range(len(xlsfile)):
    book = xlrd.open_workbook(xlsfile[n])
    sheet0 = book.sheet_by_index(0)
    sheet_name = book.sheet_names()
    print("xlsfile",xlsfile[n])
    nrows = sheet0.nrows - 3
    ncols = sheet0.ncols
    
    for i in range(nrows):
        for j in range(ncols):
            newsheet.write(i+filerow,j,sheet0.cell_value(i+3,j))
    filerow += nrows
newbook.save(r'd:\new.xls') 

a = np.arange(10)
print(a)
obj = Series([4,7,-5,3])
print(obj.values)
sdata  = {'Ohio':35000,'Texas':500,'Origen':16000,'Uth':5000}
obj3 = Series(sdata)
print(obj3)