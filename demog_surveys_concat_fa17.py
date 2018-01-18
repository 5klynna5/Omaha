import pandas as pd
import numpy as np
import ntpath
from collections import Counter
import datetime as dt
date = dt.datetime.today().strftime("%m%d%Y")

demogs_path = 'C:\\Users\\KLA\\Dropbox\\MHC OPS Absent Narratives Approach\\Evaluation (all) 2017-2018\\2017-2018 Evaluation Methods\\Surveys\\Demographic Surveys\\demographic_surveys_fa17_cleaned01182018.csv'
demogs = pd.read_csv(demogs_path, encoding = "ISO-8859-1")

sms_path = 'C:\\Users\\KLA\\Dropbox\\MHC OPS Absent Narratives Approach\\Evaluation (all) 2017-2018\\2017-2018 Evaluation Methods\\Surveys\\Demographic Surveys\\fa17_sms_demographics_cleaned.csv'
sms = pd.read_csv(sms_path, encoding = "ISO-8859-1")

del sms['Unnamed: 0']

new_columns = ['date_entered', 'response_id', 'position', 'position_other', 'pac_room_facilitator', 'transition_room_teacher', 'curriculum_specialist', 'grade_level', 'gender', 'amer_indian', 'asian', 'black', 'hispanic', 'white', 'pac_islander',  'multi_racial', 'race_other', 'race_prefer_not_say', 'entity']
sms.columns = new_columns

sms['race_combined'] = sms[['amer_indian','asian','black','hispanic','white','pac_islander','race_other','race_prefer_not_say','multi_racial']].apply(lambda x: ''.join(map(str, x)).replace("nan",""), axis=1)

sms = sms.fillna('BLANK')

sms.ix[sms.position == 'Other', 'position'] = sms.position_other
del sms['position_other']

female_list = ['a woman', 'a woman (female)', 'F', 'I am a woman', 'Mrs.', 'female/woman', 'Female', ' Female', 'female', 'Lady', 'straight female', 'woman', 'Woman', 'women', 'a woman']
male_list = ['gay man', 'male', 'man', 'M', 'Man', 'm']

female_dict = dict(zip(female_list, (['FEMALE'] * len(female_list))))
male_dict = dict(zip(male_list, (['MALE'] * len(male_list))))

sms = sms.replace({'gender': female_dict})
sms = sms.replace({'gender': male_dict})

###create race_combined variable

###convert everything upper case
sms = sms.apply(lambda x: x.str.upper())

sms['offering'] = 'sms'

sms['semester'] = 'fa17'

sms = sms.replace(to_replace='BLANK', value='')


demogs_all = pd.concat([demogs,sms])

del demogs_all['Unnamed: 0']

demogs_all.to_csv('C:\\Users\\KLA\\Dropbox\\MHC OPS Absent Narratives Approach\\Evaluation (all) 2017-2018\\2017-2018 Evaluation Methods\\Surveys\\Demographic Surveys\\demographic_surveys_cleaned_ALL_' + date + '.csv')