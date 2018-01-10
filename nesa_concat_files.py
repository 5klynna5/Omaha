import pandas as pd
print(pd.__version__)
import datetime as dt
import numpy as np     
date = dt.datetime.today().strftime("%m%d%Y")
import os
import glob

directory = 'C:\\Users\\KLA\\Dropbox\\MHC OPS Absent Narratives Approach\\Evaluation (All) 2016-2017\\Data\\NESA data\\working data\\analysis by demographic files two\\'

###this is the way to concatenate all of the rows together, so each school gets multiple rows, one for each grade
race_files = glob.glob(directory + '\\race\\*.csv')
nesa_race_math = pd.DataFrame()
list_race_math = []

nesa_race_read = pd.DataFrame()
list_race_read = []

nesa_race_science = pd.DataFrame()
list_race_science = []

nesa_race_writ = pd.DataFrame()
list_race_writ = []

for file_ in race_files:
	name = os.path.basename(file_)
	df = pd.read_csv(file_, encoding = "ISO-8859-1")
	if 'math' in name:
		list_race_math.append(df)
	elif 'read' in name:
		list_race_read.append(df)
	elif 'sci' in name:
		list_race_science.append(df)
	elif 'writ' in name:
		list_race_writ.append(df)

nesa_race_math = pd.concat(list_race_math)
nesa_race_math.to_csv(directory + 'race_math.csv')

nesa_race_read = pd.concat(list_race_read)
nesa_race_read.to_csv(directory + 'race_read.csv')

nesa_race_science = pd.concat(list_race_science)
nesa_race_science.to_csv(directory + 'race_science.csv')

nesa_race_writ = pd.concat(list_race_writ)
nesa_race_writ.to_csv(directory + 'race_writ.csv')

###this is the way to average out for each school
allFiles = glob.glob(directory + "/*.csv")
for file_ in allFiles:
	name = os.path.basename(file_)
	df = pd.read_csv(file_, encoding = "ISO-8859-1")
	df_ave = df.groupby(['entity_id'], as_index=False).mean()
	del df_ave['Unnamed: 0']
	#del df_ave['Unnamed: 0.1']
	df_ave.to_csv(directory + '\\averages by school\\average_' + name)

##now this is ell
ell_files = glob.glob(directory + '\\ell\\*.csv')
nesa_ell_math = pd.DataFrame()
list_ell_math = []

nesa_ell_read = pd.DataFrame()
list_ell_read = []

nesa_ell_science = pd.DataFrame()
list_ell_science = []

nesa_ell_writ = pd.DataFrame()
list_ell_writ = []

for file_ in ell_files:
	name = os.path.basename(file_)
	df = pd.read_csv(file_, encoding = "ISO-8859-1")
	if 'math' in name:
		list_ell_math.append(df)
	elif 'read' in name:
		list_ell_read.append(df)
	elif 'sci' in name:
		list_ell_science.append(df)
	elif 'writ' in name:
		list_ell_writ.append(df)

nesa_ell_math = pd.concat(list_ell_math)
nesa_ell_math.to_csv(directory + 'ell_math.csv')

nesa_ell_read = pd.concat(list_ell_read)
nesa_ell_read.to_csv(directory + 'ell_read.csv')

nesa_ell_science = pd.concat(list_ell_science)
nesa_ell_science.to_csv(directory + 'ell_science.csv')

nesa_ell_writ = pd.concat(list_ell_writ)
nesa_ell_writ.to_csv(directory + 'ell_writ.csv')

###this is the way to average out for each school
allFiles = glob.glob(directory + "/*.csv")
for file_ in allFiles:
	name = os.path.basename(file_)
	df = pd.read_csv(file_, encoding = "ISO-8859-1")
	df_ave = df.groupby(['entity_id'], as_index=False).mean()
	del df_ave['Unnamed: 0']
	#del df_ave['Unnamed: 0.1']
	df_ave.to_csv(directory + '\\averages by school\\average_' + name)

##now this is frl
frl_files = glob.glob(directory + '\\frl\\*.csv')
nesa_frl_math = pd.DataFrame()
list_frl_math = []

nesa_frl_read = pd.DataFrame()
list_frl_read = []

nesa_frl_science = pd.DataFrame()
list_frl_science = []

nesa_frl_writ = pd.DataFrame()
list_frl_writ = []

for file_ in frl_files:
	name = os.path.basename(file_)
	df = pd.read_csv(file_, encoding = "ISO-8859-1")
	if 'math' in name:
		list_frl_math.append(df)
	elif 'read' in name:
		list_frl_read.append(df)
	elif 'sci' in name:
		list_frl_science.append(df)
	elif 'writ' in name:
		list_frl_writ.append(df)

nesa_frl_math = pd.concat(list_frl_math)
nesa_frl_math.to_csv(directory + 'frl_math.csv')

nesa_frl_read = pd.concat(list_frl_read)
nesa_frl_read.to_csv(directory + 'frl_read.csv')

nesa_frl_science = pd.concat(list_frl_science)
nesa_frl_science.to_csv(directory + 'frl_science.csv')

nesa_frl_writ = pd.concat(list_frl_writ)
nesa_frl_writ.to_csv(directory + 'frl_writ.csv')

###this is the way to average out for each school
allFiles = glob.glob(directory + "/*.csv")
for file_ in allFiles:
	name = os.path.basename(file_)
	df = pd.read_csv(file_, encoding = "ISO-8859-1")
	df_ave = df.groupby(['entity_id'], as_index=False).mean()
	del df_ave['Unnamed: 0']
	#del df_ave['Unnamed: 0.1']
	df_ave.to_csv(directory + '\\averages by school\\average_' + name)



##now this is spec ed
spec_ed_files = glob.glob(directory + '\\spec_ed\\*.csv')
nesa_spec_ed_math = pd.DataFrame()
list_spec_ed_math = []

nesa_spec_ed_read = pd.DataFrame()
list_spec_ed_read = []

nesa_spec_ed_science = pd.DataFrame()
list_spec_ed_science = []

nesa_spec_ed_writ = pd.DataFrame()
list_spec_ed_writ = []

for file_ in spec_ed_files:
	name = os.path.basename(file_)
	df = pd.read_csv(file_, encoding = "ISO-8859-1")
	if 'math' in name:
		list_spec_ed_math.append(df)
	elif 'read' in name:
		list_spec_ed_read.append(df)
	elif 'sci' in name:
		list_spec_ed_science.append(df)
	elif 'writ' in name:
		list_spec_ed_writ.append(df)

nesa_spec_ed_math = pd.concat(list_spec_ed_math)
nesa_spec_ed_math.to_csv(directory + 'spec_ed_math.csv')

nesa_spec_ed_read = pd.concat(list_spec_ed_read)
nesa_spec_ed_read.to_csv(directory + 'spec_ed_read.csv')

nesa_spec_ed_science = pd.concat(list_spec_ed_science)
nesa_spec_ed_science.to_csv(directory + 'spec_ed_science.csv')

nesa_spec_ed_writ = pd.concat(list_spec_ed_writ)
nesa_spec_ed_writ.to_csv(directory + 'spec_ed_writ.csv')

###this is the way to average out for each school
allFiles = glob.glob(directory + "/*.csv")
for file_ in allFiles:
	name = os.path.basename(file_)
	df = pd.read_csv(file_, encoding = "ISO-8859-1")
	df_ave = df.groupby(['entity_id'], as_index=False).mean()
	del df_ave['Unnamed: 0']
	#del df_ave['Unnamed: 0.1']
	df_ave.to_csv(directory + '\\averages by school\\average_' + name)