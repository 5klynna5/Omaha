##cd C:\\Users\KLA\Dropbox\MHC OPS Absent Narratives Approach\Evaluation (All) 2015-2016\Evaluation Methods\Surveys\Story Circle Cohort

###import dependencies
import pandas as pd
import numpy as np
#import matplotlib.pyplot as plt
import ntpath
from collections import Counter
import datetime as dt
date = dt.datetime.today().strftime("%m%d%Y")

###read in survey export file

results_path = 'C:\\Users\KLA\Dropbox\\MHC OPS Absent Narratives Approach\\Evaluation (All) 2016-2017\\Evaluation Methods\\Surveys\\Demographic Surveys\Demographic_Surveys_sp17_export_06092017.csv'
results = pd.read_csv(results_path, encoding = "ISO-8859-1")

###create object for file name

results_name = ntpath.basename(results_path).rstrip('_export_03272017.csv')
results_directory = ntpath.dirname(results_path)

###drop off extra header row

results = results.drop(0)

###drop off useless columns

del results['V2']
del results['V4']
del results['V6']
del results['V7']
del results['V8']
del results['V10']
del results['LocationLatitude']
del results['LocationLongitude']
del results['LocationAccuracy']

new_columns = ['response_id', 'full_name', 'email', 'date_entered', 'offering', 'offering_other', 'position', 'position_other', 'pac_room_facilitator', 'transition_room_teacher', 'curriculum_specialist', 'grade_level', 'grade_level_other', 'gender', 'amer_indian', 'asian', 'black', 'hispanic', 'white', 'pac_islander', 'race_other', 'race_prefer_not_say', 'multi_racial', 'entity', 'entity_other']

results.columns = new_columns

del results['full_name']
del results['email']
del results['offering_other']

###replacing the other values in these columns with the write in value person provided
results.ix[results.entity == 'Other', 'entity'] = results.entity_other
del results['entity_other']

results.ix[results.grade_level == 'Other', 'grade_level'] = results.grade_level_other
del results['grade_level_other']

results.ix[results.position == 'Other', 'position'] = results.position_other
del results['position_other']

###replacing various values for gender with FEMALE AND MALE

female_list = ['a woman', 'a woman (female)', 'F', 'Female', 'female', 'Lady', 'straight female', 'woman', 'women']
male_list = ['gay man', 'male', 'man']

female_dict = dict(zip(female_list, (['FEMALE'] * len(female_list))))
male_dict = dict(zip(male_list, (['MALE'] * len(male_list))))

results = results.replace({'gender': female_dict})
results = results.replace({'gender': male_dict})

###create race_combined variable

results['race_combined'] = results[['amer_indian','asian','black','hispanic','white','pac_islander','race_other','race_prefer_not_say','multi_racial']].apply(lambda x: ''.join(map(str, x)).replace("nan",""), axis=1)


###convert everything upper case
results = results.apply(lambda x: x.str.upper())
results['semester']= 'sp17'

print(results['offering'].value_counts())

offering_dict = {'INNOCENT CLASSROOM': 'ic', 'INNOCENT CLASSROOM IN PRACTICE': 'icip', 'IMMERSION COHORT' : 'immersion', 
				'RECONSTRUCTING CURRICULUM: WHOLE SCHOOL EXPERIENCE' : 'rcwse', 'RECONSTRUCTING CURRICULUM: CLASSROOM TEACHER EXPERIENCE' : 'rccte',
				'RECONSTRUCTING CURRICULUM: FROM THEORY TO PRAXIS' : 'rcfttp', 'INCREASE STUDENT ENGAGEMENT' : 'isetan', 'STORY CIRCLE COHORT' : 'scc'}

results = results.replace({'offering': offering_dict})

###save to folder for jeff
results.to_csv('C:\\Users\\KLA\\Dropbox\\MHC OPS Absent Narratives Approach\\Evaluation (All) 2016-2017\\Evaluation Methods\\Surveys\\Demographic Surveys\\demographic_surveys_cleaned' + date + '.csv')



