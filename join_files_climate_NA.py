# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 09:58:11 2016

@author: Nadia
"""
from pandas import DataFrame, read_csv
#import csv
import pandas as pd
import numpy as np
#import selenium
import glob
#import parser

#print('Python version ' + sys.version)
#print('Pandas version ' + pd.__version__)

##pip install xlrd can be run from the command line not the interpreter!
##pip install selenium pyxl

directory = 'C:\\Users\\Nadia\SkyDrive\Evaluation\Omaha Public Schools\ClimateData\ProcessedData\Processed data' 
#

#allFiles = glob.glob(directory + "/*.xlsx")
#allFiles = glob.glob(directory + "/*.csv")
#all_data = pd.DataFrame()
#for f in allFiles:
#    df = pd.read_excel#(f,index_col=None, header=0)
#    all_data = all_data.append(df,ignore_index=True)
##    
#all_data.describe()
#
#
#
#
#table = pd.read_csv(directory + '\Intervention Group_Petal_Jazmine Franklin.csv')
#


import csv
import sys
import tempfile
import shutil

#for filename in allFiles[1:]:
#    tmp = tempfile.NamedTemporaryFile(delete=False)
#    with open(filename) as finput:
#        with open(tmp.name,'wb') as ftmp:
#            writer = csv.writer(ftmp)
#            for i, row in enumerate(csv.reader(finput)):
#                to_append = "Filename" if i == 0 else filename
#                writer.writerow(row+[to_append])
#    shutil.move(tmp.name,filename)


allFiles = glob.glob(directory + "/*.csv")
frame = pd.DataFrame()
list_ = []
for f in allFiles:
    df = pd.read_csv(f, sep =",", skiprows=range(1, 3))
    #for i in allFiles:   
    df['filename'] = f
    list_.append(df)
frame = pd.concat(list_, ignore_index = True)
frame.to_csv(directory + '/processed_climate__merged' + '.csv')


