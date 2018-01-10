import pandas as pd
print(pd.__version__)
import datetime as dt
import numpy as np     
date = dt.datetime.today().strftime("%m%d%Y")
import os
import glob

data_path = 'C:\\Users\\KLA\\Dropbox\\MHC OPS Absent Narratives Approach\\Evaluation (All) 2016-2017\\Data\\School master data\\frozen data\\schools_all_wide_small_dropped_02162017.csv'
data = pd.read_csv(data_path, encoding  = "ISO-8859-1")

demogs = ['_race_', '_frl_', '_ell_', '_spec_ed_']
subjects = ['math_', 'sci_', 'writ_', 'read_']

nesa_cols = [col for col in data.columns if '_sd' in col] + [col for col in data.columns if '_var' in col] + [col for col in data.columns if '_wtmean' in col] + [col for col in data.columns if '_z' in col]

for subject in subjects:
	nesa_cols = nesa_cols + [col for col in data.columns if subject in col]

not_nesa = data.columns - nesa_cols

data_not_nesa = data[not_nesa]

del data_not_nesa['Unnamed: 0']



directory = 'C:\\Users\\KLA\\Dropbox\\MHC OPS Absent Narratives Approach\\Evaluation (All) 2016-2017\\Data\\NESA data\\working data\\analysis files\\'

allFiles = glob.glob(directory + "/*.csv")
for file_ in allFiles:
	name = os.path.basename(file_)
	df = pd.read_csv(file_, encoding = "ISO-8859-1")
	del df['entity']
	del df['Unnamed: 0']
	#df.columns = df.columns.str.split('_', -1)
	df = pd.merge(data_not_nesa,df, on = 'entity_id')
	df.to_csv('C:\\Users\\KLA\\Dropbox\\MHC OPS Absent Narratives Approach\\Evaluation (All) 2016-2017\\Data\\NESA data\\working data\\merged analysis files\\' + name)

##do we need to rename variable names something that is consistent for analysis?
##(take last chunk after using split on '_')
###if ell or spec_ed, strip to just y/nyear
###if frl strip to just sp/fryear
###if race, more complicated... 
##also create columns for gaps (year - year)