import pandas as pd
print(pd.__version__)
import datetime as dt     
date = dt.datetime.today().strftime("%m%d%Y")

import os
import glob


directory = 'C:\\Users\\KLA\\Dropbox\\MHC OPS Absent Narratives Approach\\Evaluation (All) 2016-2017\\Data\\'

import os
for root, dirs, files in os.walk(directory):
    ##print(root)
    ##print(dirs)
    print(files[1])

import os
list_files = []
for root, dirs, files in os.walk("/mydir"):
    for file in files:
        if file.endswith(".txt"):
             list_files.append(os.path.join(root, file))


'''
allFiles = glob.glob(directory + "/*.csv")
list_files = []
for file_ in allFiles:
	name = file_.split('\\')[-1]
	list_files.append(name)
	print(name)
'''
