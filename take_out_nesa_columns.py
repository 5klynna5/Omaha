import pandas as pd
print(pd.__version__)
import datetime as dt
import numpy as np     
date = dt.datetime.today().strftime("%m%d%Y")

data_path = 'C:\\Users\\KLA\\Dropbox\\MHC OPS Absent Narratives Approach\\Evaluation (All) 2016-2017\\Data\\NESA data\\working data\\schools_all_wide_03222017_nadia.csv'
data = pd.read_csv(data_path, encoding  = "ISO-8859-1")

#print(list(data.columns))

###creating lists of all the individual things that go into the analyses designation
grades = ['3', '4', '5', '6', '7', '8', '11']
subjects = ['math_', 'sci_', 'writ_', 'read_']
demogs = ['_race_', '_frl_', '_ell_', '_spec_ed_']

##creating list of columns that involves only the columns that are necessary to look at a certain demographic analysis

nadia_cols = [col for col in data.columns if '_sd' in col] + [col for col in data.columns if '_var' in col] + [col for col in data.columns if 'wt_' in col] + [col for col in data.columns if '_wtmean' in col] + [col for col in data.columns if '_z' in col] + [col for col in data.columns if '_gr_' in col]

for subject in subjects:
	nadia_cols = nadia_cols + [col for col in data.columns if subject in col]

useful = data.columns - nadia_cols

data_useful = data[useful]

del data_useful['Unnamed: 0']
del data_useful['entity-x']

data_useful.to_csv('C:\\Users\\KLA\\Dropbox\\MHC OPS Absent Narratives Approach\\Evaluation (All) 2016-2017\\Data\\School master data\\working data\\data_without_nesa_03222017.csv')