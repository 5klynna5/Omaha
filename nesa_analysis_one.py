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
nesa_cols = ['entity_id', 'entity']
for demog in demogs:
	nesa_cols = nesa_cols +[col for col in data.columns if demog in col]

#print(nesa_cols)

##creating list of each demographic analysis for each grade
analyses = [x + y + z for x in subjects for y in grades for z in demogs]

#print(analyses)

###spitting out separate analysis files into one folder
for item in analyses:
	cols = [col for col in nesa_cols if item in col]
	cols.append('entity_id')
	cols.append('entity')
	print(cols)
	data_small = data[cols]
	data_small.to_csv('C:\\Users\\KLA\\Dropbox\\MHC OPS Absent Narratives Approach\\Evaluation (All) 2016-2017\\Data\\NESA data\\working data\\analysis_files_two\\' + item + '.csv')

'''
print(grades)

for demog in demogs:
	nesa_list = list([col for col in data.columns if demog in col])
	demog = nesa_list
	print(demog)

for grade in grades:
	nesa_list = list([col for col in data.columns if grade in col])
	grade = nesa_list
	print(grade)

for subject in subjects:
	nesa_list = list([col for col in data.columns if subject in col])
	subject = nesa_list
	print(subject)

entity_cols = ['entity', 'entity_id']


print(nesa_cols_11_)

math_11_race_data = data[math_11_race_nesa_cols]

math_11_race_data['amer_indian_gap2015-2016'] = math_11_race_data['math_11_race_amer_indian2015-2016'] / math_11_race_data['math_11_race_white2015-2016']
math_11_race_data['black_gap2014-2015'] = math_11_race_data['math_11_race_black2014-2015'] / math_11_race_data['math_11_race_white2014-2015']

print(math_11_race_data.head())

math_11_race_data.to_csv('C:\\Users\\KLA\\Dropbox\\MHC OPS Absent Narratives Approach\\Evaluation (All) 2016-2017\\Data\\NESA data\\working data\\analysis files\\math_11_race_data.csv')
'''