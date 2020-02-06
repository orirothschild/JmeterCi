# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 14:04:07 2020

@author: orir
"""
from pytest import mark
import sys
import pandas as pd
import os.path
from os import path
from pathlib import Path
import numpy as np
import glob
from xlsxwriter.utility import xl_rowcol_to_cell
@mark.orderdiff
@mark.ordergen
def test_excelCompare():
    list_of_files = glob.glob('/Users/orir/Downloads/*') # * means all if need specific format then *.csv
    sortedlist = sorted(filter(os.path.isfile, list_of_files), key=os.path.getmtime)[::-1]
    changepath = sortedlist[0]
    changepath2= sortedlist[1]

  #  out_path1 = r"C:\Users\orir\Downloads\test2.xlsx12020.xlsx"
   # out_path2 = r"C:\Users\orir\Downloads\test.xlsx142020.xlsx"

#    if path.exists(changepath) and path.exists(changepath2):
 #       os.rename(changepath,out_path1)
  #      os.rename(changepath2,out_path2)

    path_old=Path(changepath)
    path_new=Path(changepath2)

    # Read in the two excel files and fill NA
    template = pd.read_excel(path_old,na_values=np.nan,header=None)
    testSheet = pd.read_excel(path_new,na_values=np.nan,header=None)
 
    rt,ct = template.shape
    rtest,ctest = testSheet.shape
 
    df = pd.DataFrame(columns=['Cell_Location','BaseTemplate_Value','CurrentFile_Value'])
 
    for rowNo in range(max(rt,rtest)):
        for colNo in range(max(ct,ctest)):
            # Fetching the template value at a cell
            try:
                template_val = template.iloc[rowNo,colNo]
            except:
                template_val = np.nan
        
            # Fetching the testsheet value at a cell
            try:
                testSheet_val = testSheet.iloc[rowNo,colNo]
            except:
                testSheet_val = np.nan
            
            # Comparing the values
            if (str(template_val)!=str(testSheet_val)):
                cell = xl_rowcol_to_cell(rowNo, colNo)
                dfTemp = pd.DataFrame([[cell,template_val,testSheet_val]],
                                      columns= ['Cell_Location','BaseTemplate_Value','CurrentFile_Value'])
                df = df.append(dfTemp)    
   
    print(df)
    export_csv = df.to_csv(r'C:\Users\orir\Downloads\export_dataframe.csv', index = None, header=True) #Don't forget to add '.csv' at the end of the path
    assert True
