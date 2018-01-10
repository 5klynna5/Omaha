import pandas as pd
print(pd.__version__)
import datetime as dt
import numpy as np     
date = dt.datetime.today().strftime("%m%d%Y")
import os
import glob

data_path = 'C:\\Users\\KLA\\Dropbox\\MHC OPS Absent Narratives Approach\\Evaluation (All) 2016-2017\\Data\\NESA data\\working data\\schools_all_wide_03222017_nadia.csv'
data = pd.read_csv(data_path, encoding  = "ISO-8859-1")


demogs = ['_race_', '_frl_', '_ell_', '_spec_ed_']
subjects = ['math_', 'sci_', 'writ_', 'read_']

nadia_cols = [col for col in data.columns if '_sd' in col] + [col for col in data.columns if '_var' in col] + [col for col in data.columns if 'wt_' in col] + [col for col in data.columns if '_wtmean' in col] + [col for col in data.columns if '_z' in col] + [col for col in data.columns if '_gr_' in col]

for subject in subjects:
	nadia_cols = nadia_cols + [col for col in data.columns if subject in col]

useful = data.columns - nadia_cols

data_useful = data[useful]

del data_useful['Unnamed: 0']
del data_useful['entity-x']

print(list(data_useful.columns))


directory = 'C:\\Users\\KLA\\Dropbox\\MHC OPS Absent Narratives Approach\\Evaluation (All) 2016-2017\\Data\\NESA data\\working data\\analysis_files_two\\'


allFiles = glob.glob(directory + "/*.csv")
for file_ in allFiles:
	name = os.path.basename(file_)
	df = pd.read_csv(file_, encoding = "ISO-8859-1")
	del df['entity']
	del df['Unnamed: 0']
	analysis = name.split(".", 1)[0]
	nesa = [col for col in df.columns if analysis in col]
	nesa_replaced = []
	#print(nesa)
	for item in nesa:
		item = item.replace(analysis,"nesa_")
		nesa_replaced.append(item)
		#print(nesa_replaced)
		#df.columns = df.columns.str.split('_', -1)
	nesa_dict = dict(zip(nesa, nesa_replaced))
	df = df.rename(columns= nesa_dict)
	df = pd.merge(data_useful,df, on = 'entity_id')
	df.to_csv('C:\\Users\\KLA\\Dropbox\\MHC OPS Absent Narratives Approach\\Evaluation (All) 2016-2017\\Data\\NESA data\\working data\\merged_analysis_files_two\\' + name)


