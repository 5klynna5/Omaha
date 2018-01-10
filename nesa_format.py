import pandas as pd
print(pd.__version__)
import datetime as dt     
date = dt.datetime.today().strftime("%m%d%Y")

import os
import glob


directory = 'C:\\Users\\KLA\\Dropbox\\MHC OPS Absent Narratives Approach\\Evaluation (All) 2016-2017\\Data\\NESA data\\working data\\copied tables\\'

allFiles = glob.glob(directory + "/*.csv")
list_files = []
for file_ in allFiles:
	name = file_.split('\\')[-1]
	list_files.append(name)

for item in list_files:
	nesa_df = pd.read_csv(directory + item, encoding = "ISO-8859-1")
	simple_name = item.rstrip('.csv')
	school_year = simple_name.split('_')[1]
	level = simple_name.split('_')[2]
	subject = simple_name.split('_')[3]
	demographic_type = simple_name.split('_')[-1]

#path_nesa = 'C:\\Users\\KLA\\Dropbox\\MHC OPS Absent Narratives Approach\\Evaluation (All) 2016-2017\\Data\\NESA data\\working data\\copied tables\\'


	nesa_df.columns = [['variable','average_scale_score']]

##for the frl data frames, this replace code works to find and replace with smaller variable names so that the code below works

	nesa_df = nesa_df.replace(to_replace = ['Self-pay', 'Free/Reduced', 'No', 'Yes', '(blank)'], value = ['SP', 'FR', 'N', 'Y', None])


	nesa_values = nesa_df['variable'].value_counts().index.tolist()

	nesa_schools = [item for item in nesa_values if len(item) >= 3]
	nesa_grades_demogs = [item for item in nesa_values if len(item) < 3]
	nesa_grades = [item for item in nesa_grades_demogs if item in ['3','4', '5', '6', '7', '8', '9', '10', '11', '12', '03', '04', '05', '06', '07', '08', '09']]
	nesa_demogs = [item for item in nesa_grades_demogs if item  not in ['3','4', '5', '6', '7', '8', '9', '10', '11', '12', '03', '04', '05', '06', '07', '08', '09']]


	nesa_df['school_year'] = school_year

###create school column where school is filled down through each row until next school

	def keep_school(school):
		if school in nesa_schools:
			return school
		else:
			return None

	keep = lambda x : keep_school(x)

	nesa_df['entity'] = nesa_df['variable'].map(keep)




#nesa_df['school'] = nesa_df['school'].fillna(method='ffill')
#### making ENTITY_TOTAL rows




###creating grade column


	def get_grade(item):
		if item in nesa_grades:
			return item
		else:
			return None

	grade = lambda x: get_grade(x)

	nesa_df['grade'] = nesa_df['variable'].map(grade)

#nesa_df['grade'] = nesa_df['grade'].fillna(method='ffill')

####creating demographic column


	def get_demog(item):
		if item in nesa_demogs:
			return item
		else:
			return None

	demog = lambda x: get_demog(x)

	nesa_df['demographic'] = nesa_df['variable'].map(demog)


#####

	del nesa_df['variable']
#nesa_df.rename(columns = {'Average of Scale Score':'average_scale_score'}, inplace = True)


	nesa_df['entity'] = nesa_df['entity'].fillna(method='ffill')



###just need to do this once per level and school year
	nesa_df['subject'] = subject

	nesa_totals = nesa_df.loc[nesa_df['demographic'].isnull()]

	del nesa_totals['demographic']
	nesa_totals['grade'] = nesa_totals['grade'].fillna('ALL')



	nesa_totals.to_csv('C:\\Users\\KLA\\Dropbox\\MHC OPS Absent Narratives Approach\\Evaluation (All) 2016-2017\\Data\\NESA data\\working data\\totals files\\nesa_totals_' + school_year + '_' + level + '_' + subject + '.csv')


	nesa_df['grade'] = nesa_df['grade'].fillna(method='ffill')

	nesa_df = nesa_df.loc[nesa_df['demographic'].notnull()]

	nesa_df['demographic_type'] = demographic_type


	nesa_df.to_csv('C:\\Users\\KLA\\Dropbox\\MHC OPS Absent Narratives Approach\\Evaluation (All) 2016-2017\\Data\\NESA data\\working data\\formatted files\\nesa_raw_' + subject + '_' + school_year + '_' + level + '_' + demographic_type + '.csv')

