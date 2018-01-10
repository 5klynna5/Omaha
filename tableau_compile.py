import pandas as pd
print(pd.__version__)
import datetime as dt
import numpy as np     
date = dt.datetime.today().strftime("%m%d%Y")

partic_path = 'C:\\Users\\KLA\\Dropbox\\MHC OPS Absent Narratives Approach\\Evaluation (All) 2016-2017\\Data\\Participation Data\\frozen data\\cohort_not_cohort_attended_04182017.csv'

data = pd.read_csv(partic_path, encoding = "ISO-8859-1")

print(data.columns)

data['first_name'] = data['full_name'].apply(lambda x: pd.Series(x.split(' ')))[0]
data['last_name'] = data['full_name'].apply(lambda x: pd.Series(x.split(' ')))[1]


data['lastfirstname'] = data['last_name'] + ', ' + data['first_name']

del data['first_name']
del data['last_name']

del data['Unnamed: 0']

data['simplesemester'] = data['semester'].apply(lambda x: x[:-5])

data['entry_id'] = data['person_id'].astype(str) + data['program_id'].astype(str)

print(data.head())

data.to_csv('C:\\Users\\KLA\\Dropbox\\MHC OPS Absent Narratives Approach\\Evaluation (All) 2016-2017\\Data\\Tableau School Profiles\\tableau_compiled_' + date + '.csv')
