# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 16:40:12 2020

@author: orir

rename file
"""

import os
import datetime

Current_Date = datetime.datetime.today().strftime ('%d-%b-%Y')
os.rename(r'C:\Users\orir\Downloads\ניהול הזמנה_יום שלישי 14 ינואר 2020.xlsx',r'C:\Users\orir\Downloads\test.xlsx' + str(Current_Date) + '.xlsx')
os.rename(r'C:\Users\orir\Downloads\ניהול הזמנה_יום שלישי 14 ינואר 2020 (1).xlsx',r'C:\Users\orir\Downloads\test2.xlsx' + str(Current_Date) + '.xlsx')