#!/usr/bin/env python
#-*- coding:utf-8 -*-
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

xlsdir = unicode('d:\周报','utf-8')
xlsfile = GetFileList(xlsdir)
newbook = xlwt.Workbook(encoding='utf-8', style_compression=0)
newsheet = newbook.add_sheet('sheet1', cell_overwrite_ok=True)
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

newfile = r'd:\研发部门周报汇总_201808.xls'
newbook.save(newfile.decode('utf-8')) 
