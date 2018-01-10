import pandas as pd
print(pd.__version__)
import datetime as dt
import numpy as np
date = dt.datetime.today().strftime("%m%d%Y")

staff_nums_path = 'C:\\Users\\KLA\\Dropbox\\MHC OPS Absent Narratives Approach\\Evaluation (all) 2017-2018\\2017-2018 Data\\Staff counts\\frozen data\\2016-ops-payroll-data_staff_counts_12122017.csv'
staff_nums = pd.read_csv(staff_nums_path, encoding = "ISO-8859-1")

del staff_nums['school']
staff_nums = pd.DataFrame(pd.pivot_table(staff_nums, index = ['entity', 'entity_id'], values = ['staff_count'], aggfunc = 'sum')).reset_index()

cal_events_path = 'C:\\Users\\KLA\\Dropbox\\MHC OPS Absent Narratives Approach\\Evaluation (all) 2017-2018\\2017-2018 Data\\Participation Data\\School Based Events\\frozen data\\events_calendar_all_01082018.csv'
cal_events = pd.read_csv(cal_events_path, encoding = "ISO-8859-1")

cal_events = pd.DataFrame(pd.pivot_table(cal_events, index = ["entity", "entity_id"], values = ['staff_attendance'], aggfunc = 'max')).reset_index()



part_data_path = 'C:\\Users\\KLA\\Dropbox\\MHC OPS Absent Narratives Approach\\Evaluation (all) 2017-2018\\2017-2018 Data\\Participation Data\\frozen_data\\cohort_not_cohort_attended_08142017.csv'
part_data = pd.read_csv(part_data_path, encoding = "ISO-8859-1")

print(part_data['person_id'].nunique())

'''

part_data_schools = pd.DataFrame(pd.pivot_table(part_data,index=["entity", 'entity_id'], values=["person_id"],aggfunc= pd.Series.nunique)).reset_index()


data_schools = pd.merge(cal_events, staff_nums, how = 'left', on = 'entity_id')

del data_schools['entity_y']

data_schools.columns = ['entity', 'entity_id', 'highest_cal_attend','total_staff_2017']

data_schools['highest_cal_attend'] = (data_schools['highest_cal_attend'].fillna((data_schools['total_staff_2017'])*.5)).apply(lambda x: np.rint(x))

data_schools = pd.merge(data_schools, part_data_schools, how = 'outer', on = ['entity_id'])

del data_schools['entity_y']
data_schools.columns = ['entity', 'entity_id', 'highest_cal_attend','total_staff_2017','num_unique_educs_in_part_data']
print(data_schools.head())

data_schools['part_num_to_use'] = data_schools[['highest_cal_attend', 'num_unique_educs_in_part_data']].max(axis=1)

data_schools.to_csv('C:\\Users\\KLA\\Dropbox\\MHC OPS Absent Narratives Approach\\Evaluation (all) 2017-2018\\2017-2018 Data\\Participation Data\\working_data\\schools_participation_01082018.csv')

##nope not working right, how do we get no duplicates??
'''