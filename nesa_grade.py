import pandas as pd
print(pd.__version__)
import datetime as dt     
date = dt.datetime.today().strftime("%m%d%Y")

nesa_grade_path = 'C:\\Users\\KLA\\Dropbox\\MHC OPS Absent Narratives Approach\\Evaluation (All) 2016-2017\\Data\\NESA data\\working data\\wide format files\\nesa_5.csv'

nesa_grade = pd.read_csv(nesa_grade_path)

print(list(nesa_grade.columns))

list_races = ['amer_indian', 'asian', 'black', 'hispanic', 'multi_racial', 'pac_islander', 'white']


###create sum scale score, we can't really do this if we don't know total test takers  = total enrolled

#for item in list_races:
	#nesa_grade['sum_math_' + item + '_score'] = nesa_grade[item] * nesa_grade['math_5_race_' + item]

#print(nesa_grade.head())

##create gap percent score

non_white = list_races[:6]

for item in non_white:
	nesa_grade['gap_math_' + item + '_score'] =  nesa_grade['math_5_race_' + item] / nesa_grade['math_5_race_white']

del nesa_grade['Unnamed: 0']
print(nesa_grade.head())

nesa_grade.to_csv('C:\\Users\\KLA\\Dropbox\\MHC OPS Absent Narratives Approach\\Evaluation (All) 2016-2017\\Data\\NESA data\\working data\\wide format files\\nesa_5_gap.csv')