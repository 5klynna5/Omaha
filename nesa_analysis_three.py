import pandas as pd
print(pd.__version__)
import datetime as dt
import numpy as np     
date = dt.datetime.today().strftime("%m%d%Y")
import os
import glob

directory = 'C:\\Users\\KLA\\Dropbox\\MHC OPS Absent Narratives Approach\\Evaluation (All) 2016-2017\\Data\\NESA data\\working data\\merged_analysis_files_two\\'

school_years = ['2011-2012', '2012-2013', '2013-2014', '2014-2015', '2015-2016']
poc = ['amer_indian', 'pac_islander', 'black', 'multi_racial', 'asian', 'hispanic']

race_year = [x + y for x in poc for y in school_years]

print(race_year)


allFiles = glob.glob(directory + "/*.csv")
for file_ in allFiles:
	name = os.path.basename(file_)
	df = pd.read_csv(file_, encoding = "ISO-8859-1")
	analysis = name.split(".", 1)[0]
	del df['Unnamed: 0']
	if 'race' in analysis:
		for year in school_years:
			for race in poc:
				if 'nesa_' + race + year in df.columns:
					df[race + '_gap' + year] = df['nesa_' + race + year] / df['nesa_white' + year]	
				else:
					df[race + '_gap' + year] = None
		for race in poc:
			df[race + '_gap_change2012-2013'] = df[race + '_gap2012-2013'] - df[race + '_gap2011-2012']
			df[race + '_gap_change2013-2014'] = df[race + '_gap2013-2014'] - df[race + '_gap2012-2013']
			df[race + '_gap_change2014-2015'] = df[race + '_gap2014-2015'] - df[race + '_gap2013-2014']
			df[race + '_gap_change2015-2016'] = df[race + '_gap2015-2016'] - df[race + '_gap2014-2015']
			if race + '_gap2011-2012' in df.columns and race + '_gap2014-2015' in df.columns:
				df[race + '_gap_change_total'] = df[race + '_gap2014-2015'] - df[race + '_gap2011-2012']
			else: 
				df[race + '_gap_change_total'] = None
		df.to_csv('C:\\Users\\KLA\\Dropbox\\MHC OPS Absent Narratives Approach\\Evaluation (All) 2016-2017\\Data\\NESA data\\working data\\analysis by demographic files two\\race\\' + name)
	
	elif 'frl' in analysis:
		for year in school_years:
			if 'nesa_fr' + year in df.columns:
				df['gap_' + year] = df['nesa_fr' + year] / df['nesa_sp' + year]
			else:
				df['gap_' + year] = None
		df['gap_change_2012-2013'] = df['gap_2012-2013'] - df['gap_2011-2012']
		df['gap_change_2013-2014'] = df['gap_2013-2014'] - df['gap_2012-2013']
		df['gap_change_2014-2015'] = df['gap_2014-2015'] - df['gap_2013-2014']
		df['gap_change_2015-2016'] = df['gap_2015-2016'] - df['gap_2014-2015']
		if 'gap_2014-2015' in df.columns and 'gap_2011-2012' in df.columns:
			df['gap_change_total'] = df['gap_2014-2015'] - df['gap_2011-2012']
		else:
			df['gap_change_total'] = None
		df.to_csv('C:\\Users\\KLA\\Dropbox\\MHC OPS Absent Narratives Approach\\Evaluation (All) 2016-2017\\Data\\NESA data\\working data\\analysis by demographic files two\\frl\\' + name)

	else:
		for year in school_years:
			if 'nesa_n' + year in df.columns:
				df['gap_' + year] = df['nesa_y' + year] / df['nesa_n' + year]
			else:
				df['gap_' + year] = None
		df['gap_change_2012-2013'] = df['gap_2012-2013'] - df['gap_2011-2012']
		df['gap_change_2013-2014'] = df['gap_2013-2014'] - df['gap_2012-2013']
		df['gap_change_2014-2015'] = df['gap_2014-2015'] - df['gap_2013-2014']
		df['gap_change_2015-2016'] = df['gap_2015-2016'] - df['gap_2014-2015']
		if 'gap_2014-2015' in df.columns and 'gap_2011-2012' in df.columns:
			df['gap_change_total'] = df['gap_2014-2015'] - df['gap_2011-2012']
		else:
			df['gap_change_total'] = None
		#df['gap_change_total'] = df['gap_2014-2015'] - df['gap_2011-2012']
		if 'ell' in analysis:
			df.to_csv('C:\\Users\\KLA\\Dropbox\\MHC OPS Absent Narratives Approach\\Evaluation (All) 2016-2017\\Data\\NESA data\\working data\\analysis by demographic files two\\ell\\' + name)
		else:
			df.to_csv('C:\\Users\\KLA\\Dropbox\\MHC OPS Absent Narratives Approach\\Evaluation (All) 2016-2017\\Data\\NESA data\\working data\\analysis by demographic files two\\spec_ed\\' + name)	

	