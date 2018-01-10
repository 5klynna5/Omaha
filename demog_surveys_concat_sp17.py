import pandas as pd
import numpy as np
import ntpath
from collections import Counter
import datetime as dt
date = dt.datetime.today().strftime("%m%d%Y")

demogs_path = 'C:\\Users\KLA\Dropbox\\MHC OPS Absent Narratives Approach\\Evaluation (All) 2016-2017\\Evaluation Methods\\Surveys\\Demographic Surveys\\demographic_surveys_cleaned\\demographic_surveys_cleaned06092017.csv'
demogs = pd.read_csv(demogs_path, encoding = "ISO-8859-1")

sms_path = 'C:\\Users\KLA\Dropbox\\MHC OPS Absent Narratives Approach\\Evaluation (All) 2016-2017\\Evaluation Methods\\Surveys\\Demographic Surveys\\demographic_surveys_cleaned\\sms_sp17_survey_demographics.csv'
sms = pd.read_csv(sms_path, encoding = "ISO-8859-1")

del sms['Unnamed: 0']

sms['response_id'] = sms['response_ID']
sms['transition_room_teacher'] = sms['transition_room']

del sms['response_ID']
del sms['transition_room']


sms['race_combined'] = sms[['amer_indian','asian','black','hispanic','white','pac_islander','race_other','race_prefer_not_say','multi_racial']].apply(lambda x: ''.join(map(str, x)).replace("nan",""), axis=1)

sms = sms.fillna('BLANK')

sms.ix[sms.position == 'Other', 'position'] = sms.position_other
del sms['position_other']

female_list = ['a woman', 'a woman (female)', 'F', 'Female', 'female', 'Lady', 'straight female', 'woman', 'women']
male_list = ['gay man', 'male', 'man']

female_dict = dict(zip(female_list, (['FEMALE'] * len(female_list))))
male_dict = dict(zip(male_list, (['MALE'] * len(male_list))))

sms = sms.replace({'gender': female_dict})
sms = sms.replace({'gender': male_dict})

###create race_combined variable

###convert everything upper case
sms = sms.apply(lambda x: x.str.upper())

sms['offering'] = 'sms'

sms['semester'] = sms['semester'].str.lower()

sms = sms.replace(to_replace='BLANK', value='')


demogs_all = pd.concat([demogs,sms])

del demogs_all['Unnamed: 0']

demogs_all.to_csv('C:\\Users\KLA\Dropbox\\MHC OPS Absent Narratives Approach\\Evaluation (All) 2016-2017\\Evaluation Methods\\Surveys\\Demographic Surveys\\demographic_surveys_cleaned\\demographic_surveys_cleaned_ALL_06122017.csv')