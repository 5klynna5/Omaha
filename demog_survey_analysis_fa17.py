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

results_path = 'C:\\Users\\KLA\\Dropbox\\MHC OPS Absent Narratives Approach\\Evaluation (all) 2017-2018\\2017-2018 Evaluation Methods\\Surveys\\Demographic Surveys\\demog_surveys_export_fa17_01182018.csv'
results = pd.read_csv(results_path, encoding = "ISO-8859-1")

###create object for file name

#results_name = ntpath.basename(results_path).rstrip('_01182018.csv')
results_directory = ntpath.dirname(results_path)

###drop off extra header row

results = results.drop(0)
results = results.drop(1)



###drop off useless columns

del results['Status']
del results['IPAddress']
del results['Progress']
del results['Duration (in seconds)']
del results['Finished']
del results['StartDate']
del results['EndDate']
del results['LocationLatitude']
del results['LocationLongitude']
del results['DistributionChannel']
del results['UserLanguage']
del results['ExternalReference']
del results['RecipientFirstName']
del results['RecipientLastName']
del results['RecipientEmail']

print(results.head())
print(results.columns)


new_columns = ['date_entered', 'response_id', 'offering', 'offering_other', 'position', 'position_other', 'pac_room_facilitator', 'transition_room_teacher', 'curriculum_specialist', 'grade_level', 'grade_level_other', 'gender', 'amer_indian', 'asian', 'black', 'hispanic', 'pac_islander', 'white', 'multi_racial', 'race_other', 'race_prefer_not_say', 'entity', 'entity_other']

results.columns = new_columns

###replacing the other values in these columns with the write in value person provided
results.ix[results.entity == 'Other', 'entity'] = results.entity_other
del results['entity_other']

results.ix[results.grade_level == 'Other', 'grade_level'] = results.grade_level_other
del results['grade_level_other']

results.ix[results.position == 'Other', 'position'] = results.position_other
del results['position_other']

###replacing various values for gender with FEMALE AND MALE

female_list = ['a woman', 'a woman (female)', 'F', 'I am a woman', 'Mrs.', 'female/woman', 'Female', ' Female', 'female', 'Lady', 'straight female', 'woman', 'Woman', 'women', 'a woman']
male_list = ['gay man', 'male', 'man', 'M', 'Man', 'm']

female_dict = dict(zip(female_list, (['FEMALE'] * len(female_list))))
male_dict = dict(zip(male_list, (['MALE'] * len(male_list))))

results = results.replace({'gender': female_dict})
results = results.replace({'gender': male_dict})

###create race_combined variable

results['race_combined'] = results[['amer_indian','asian','black','hispanic','white','pac_islander','race_other','race_prefer_not_say','multi_racial']].apply(lambda x: ''.join(map(str, x)).replace("nan",""), axis=1)


###convert everything upper case

results = results.apply(lambda x: x.str.upper())
results['semester']= 'fa17'

print(results['offering'].value_counts())

offering_dict = {'INNOCENT CLASSROOM': 'ic', 'INNOCENT CLASSROOM IN PRACTICE': 'icip', 'IMMERSION COHORT' : 'immersion', 
				'RECONSTRUCTING CURRICULUM: WHOLE SCHOOL EXPERIENCE' : 'rcwse', 'RECONSTRUCTING CURRICULUM: CLASSROOM TEACHER EXPERIENCE' : 'rccte',
				'RECONSTRUCTING CURRICULUM: FROM THEORY TO PRAXIS' : 'rcfttp', 'INCREASE STUDENT ENGAGEMENT' : 'isetan', 'STORY CIRCLE COHORT' : 'scc'}

results = results.replace({'offering': offering_dict})

###save to folder
results.to_csv('C:\\Users\\KLA\\Dropbox\\MHC OPS Absent Narratives Approach\\Evaluation (all) 2017-2018\\2017-2018 Evaluation Methods\\Surveys\\Demographic Surveys\\demographic_surveys_fa17_cleaned' + date + '.csv')



