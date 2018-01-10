import pandas as pd
print(pd.__version__)
import datetime as dt     
date = dt.datetime.today().strftime("%m%d%Y")


import numpy as np

###load in all simplified enrollment data for each year

path_enroll_11_12 = 'C:\\Users\\KLA\\Dropbox\\MHC OPS Absent Narratives Approach\Evaluation (All) 2016-2017\\Data\\School master data\\working data\\Official Fall Data (Demographics)\\school_data_11_12_KA.csv'
enroll_11_12_df = pd.read_csv(path_enroll_11_12, encoding = "ISO-8859-1")

path_enroll_12_13 = 'C:\\Users\\KLA\\Dropbox\\MHC OPS Absent Narratives Approach\Evaluation (All) 2016-2017\\Data\\School master data\\working data\\Official Fall Data (Demographics)\\school_data_12_13_KA.csv'
enroll_12_13_df = pd.read_csv(path_enroll_12_13, encoding = "ISO-8859-1")

path_enroll_13_14 = 'C:\\Users\\KLA\\Dropbox\\MHC OPS Absent Narratives Approach\Evaluation (All) 2016-2017\\Data\\School master data\\working data\\Official Fall Data (Demographics)\\school_data_13_14_KA.csv'
enroll_13_14_df = pd.read_csv(path_enroll_13_14, encoding = "ISO-8859-1")

path_enroll_14_15 = 'C:\\Users\\KLA\\Dropbox\\MHC OPS Absent Narratives Approach\Evaluation (All) 2016-2017\\Data\\School master data\\working data\\Official Fall Data (Demographics)\\school_data_14_15_KA.csv'
enroll_14_15_df = pd.read_csv(path_enroll_14_15, encoding = "ISO-8859-1")

path_enroll_15_16 = 'C:\\Users\\KLA\\Dropbox\\MHC OPS Absent Narratives Approach\Evaluation (All) 2016-2017\\Data\\School master data\\working data\\Official Fall Data (Demographics)\\school_data_15_16_KA.csv'
enroll_15_16_df = pd.read_csv(path_enroll_15_16, encoding = "ISO-8859-1")

##convert numeric columns to numeric, replacing dashes with 0 and taking out commas in the middle of numbers

list_to_numeric = ['total_enroll','projected_enroll','hispanic','amer_indian','black','white','asian','pac_islander','multi_racial','total_minority','frl','ell','spec_ed','gifted']

for col in list_to_numeric:
	enroll_11_12_df[col] = enroll_11_12_df[col].replace(to_replace=['(^|\s+)-(\s+|$)', ','], value = ['0',''], regex=True).apply(lambda x: pd.to_numeric(x, errors = 'coerce'))
	enroll_12_13_df[col] = enroll_12_13_df[col].apply(lambda x: pd.to_numeric(x, errors = 'coerce'))
	enroll_13_14_df[col] = enroll_13_14_df[col].replace(to_replace=['(^|\s+)-(\s+|$)', ','], value = ['0',''], regex=True).apply(lambda x: pd.to_numeric(x, errors = 'coerce'))
	enroll_14_15_df[col] = enroll_14_15_df[col].replace(to_replace=['(^|\s+)-(\s+|$)', ','], value = ['0',''], regex=True).apply(lambda x: pd.to_numeric(x, errors = 'coerce'))
	enroll_15_16_df[col] = enroll_15_16_df[col].replace(to_replace=['(^|\s+)-(\s+|$)', ','], value = ['0',''], regex=True).apply(lambda x: pd.to_numeric(x, errors = 'coerce'))


#enroll_12_13_df.to_csv('./enroll_12_13_grouped.csv')

##combine each year's data frame into one big data frame

enroll_all_list = [enroll_11_12_df, enroll_12_13_df, enroll_13_14_df, enroll_14_15_df, enroll_15_16_df]
enroll_all_df = pd.concat(enroll_all_list)

del enroll_all_df['entity_id']

enroll_all_df.to_csv('./enroll_concat_test.csv')



##loading in and merging in the entity id data that jeff made, which includes the canonical entity ids and names

entity_df = pd.read_csv('C:\\Users\KLA\Dropbox\MHC OPS Absent Narratives Approach\Evaluation (All) 2016-2017\Data\School master data\\working data\\fall_data_entity_codebook.csv')


#enroll_all_df.to_csv('C:\\Users\KLA\Dropbox\MHC OPS Absent Narratives Approach\Evaluation (All) 2016-2017\Data\School master data\\frozen data\\school_data_all.csv')
schools = enroll_all_df.merge(entity_df, how='inner', on=['school'])

del schools['Unnamed: 16']
del schools['Unnamed: 17']
del schools['Unnamed: 18']
del schools['entity_type']

schools.to_csv('C:\\Users\KLA\Dropbox\MHC OPS Absent Narratives Approach\Evaluation (All) 2016-2017\Data\School master data\\working data\\schools_demogs_test_' + date + '.csv')

schools = schools.groupby(['school_year', 'entity_id'], as_index=False).sum()

schools.to_csv('C:\\Users\KLA\Dropbox\MHC OPS Absent Narratives Approach\Evaluation (All) 2016-2017\Data\School master data\\working data\\schools_demogs_grouped_' + date + '.csv')

#loading in the behavior data (attendance, suspension, mobility)

path_behavior_no_doubles = 'C:\\Users\KLA\Dropbox\MHC OPS Absent Narratives Approach\Evaluation (All) 2016-2017\Data\School master data\working data\Official Fall Data (Demographics)\\suspend_mobility_attend_no_doubles_11082016.csv'
behavior_no_doubles = pd.read_csv(path_behavior_no_doubles, encoding = "ISO-8859-1")


behavior_no_doubles = behavior_no_doubles.merge(entity_df, how='inner', on = 'school')


behavior_no_doubles.to_csv('C:\\Users\\KLA\\Dropbox\\MHC OPS Absent Narratives Approach\\Evaluation (All) 2016-2017\\Data\\School master data\\working data\\Official Fall Data (Demographics)\\behavior_no_doubles' + date +'_.csv')


#full_school_data.replace(to_replace=['  -    ','-', ' - ', ' -   '], value = [0,0,0,0], inplace = True) ##code below does same thing
#full_school_data.replace(to_replace='(^|\s+)-(\s+|$)', value = 0, inplace=True, regex=True)

##converting the mobility percent and attendance percent columns to decimals instead of some decimals, some percents
behavior_no_doubles['mobility_percent'] = behavior_no_doubles['mobility_percent'].astype(str).apply(lambda x: x.rstrip('%'))
behavior_no_doubles['attend_percent'] = behavior_no_doubles['attend_percent'].astype(str).apply(lambda x: x.rstrip('%'))


behavior_no_doubles['mobility_percent'] = behavior_no_doubles['mobility_percent'].apply(lambda x: pd.to_numeric(x, errors='coerce'))
behavior_no_doubles['attend_percent'] = behavior_no_doubles['attend_percent'].apply(lambda x: pd.to_numeric(x, errors='coerce'))


def convert_percents(number):
	if number > 0:
		return number/100
	else:
		return number

f = lambda x: convert_percents(x)

def convert_percents_two(number):
	if number < 0.01:
		return number*100
	else:
		return number

ftwo = lambda x: convert_percents_two(x)


behavior_no_doubles['mobility_percent'] = behavior_no_doubles['mobility_percent'].map(f)
behavior_no_doubles['attend_percent'] = behavior_no_doubles['attend_percent'].map(f)
behavior_no_doubles['mobility_percent'] = behavior_no_doubles['mobility_percent'].map(ftwo)
behavior_no_doubles['attend_percent'] = behavior_no_doubles['attend_percent'].map(ftwo)

schools_behavior_no_doubles = schools.merge(behavior_no_doubles, how = 'left', on = ['school_year', 'entity_id'])


schools_behavior_no_doubles.to_csv('C:\\Users\\KLA\\Dropbox\\MHC OPS Absent Narratives Approach\\Evaluation (All) 2016-2017\\Data\\School master data\\working data\\Official Fall Data (Demographics)\\behavior_schools_no_doubles' + date +'.csv')


behavior_doubles_path = 'C:\\Users\KLA\Dropbox\MHC OPS Absent Narratives Approach\Evaluation (All) 2016-2017\Data\School master data\working data\Official Fall Data (Demographics)\\suspend_mobility_attend_KA_doubles_grouped_11082016.csv'
behavior_doubles = pd.read_csv(behavior_doubles_path, encoding = "ISO-8859-1")

del behavior_doubles['Unnamed: 0']

behavior_doubles['mobility_percent'] = behavior_doubles['mobility_num_calc'] / behavior_doubles['total_enroll']

schools_behavior = schools_behavior_no_doubles.merge(behavior_doubles, how = 'left', on = ['school_year', 'entity_id'])

schools_behavior.to_csv('C:\\Users\\KLA\\Dropbox\\MHC OPS Absent Narratives Approach\\Evaluation (All) 2016-2017\\Data\\School master data\\working data\\Official Fall Data (Demographics)\\behavior_schools' + date +'.csv')
##splitting mobility and suspension into seperate data frame, merging them into master data set



del schools_behavior['total_enroll_y']

schools_behavior = schools_behavior.rename(columns = {'total_enroll_x' : 'total_enroll'})

schools_behavior['suspend_num'] = schools_behavior['suspend_num_x'].fillna(schools_behavior['suspend_num_y'])

schools_behavior['mobility_percent'] = schools_behavior['mobility_percent_x'].fillna(schools_behavior['mobility_percent_y'])

schools_behavior['attend_percent'] = schools_behavior['attend_percent'].fillna(schools_behavior['attend_num_calc'] / schools_behavior['total_enroll'])

del schools_behavior['suspend_num_x']
del schools_behavior['suspend_num_y']
del schools_behavior['entity_x']
del schools_behavior['entity_y']
del schools_behavior['mobility_num_calc']
del schools_behavior['attend_num_calc']
del schools_behavior['school']
del schools_behavior['mobility_percent_x']
del schools_behavior['mobility_percent_y']


schools_behavior.to_csv('C:\\Users\\KLA\\Dropbox\\MHC OPS Absent Narratives Approach\\Evaluation (All) 2016-2017\\Data\\School master data\\working data\\Official Fall Data (Demographics)\\behavior_schools_combined_' + date +'.csv')

##merge in entity names and educator data

path_educ = 'C:\\Users\KLA\Dropbox\MHC OPS Absent Narratives Approach\Evaluation (All) 2016-2017\Data\School master data\\working data\\ops_staff_count_by_school_fall_data.csv'
educ_df = pd.read_csv(path_educ, encoding = "ISO-8859-1")

educ_df = educ_df[['entity_id', 'school_year', 'staff_count']]
entity_df = entity_df[['entity_id', 'entity']]


entity_df = entity_df.drop_duplicates()


school_demogs = schools_behavior.merge(entity_df, how = 'left', on = ['entity_id'])
school_demogs = school_demogs.merge(educ_df, how = 'left', on = ['entity_id', 'school_year'])


school_demogs.to_csv('C:\\Users\KLA\Dropbox\MHC OPS Absent Narratives Approach\Evaluation (All) 2016-2017\Data\School master data\\working data\\schools_demogs_' + date + '.csv')



##merge in participation data##

part_by_school_path = 'C:\\Users\KLA\Dropbox\MHC OPS Absent Narratives Approach\Evaluation (All) 2016-2017\Data\School master data\\frozen data\offerings_core_offerings_count_by_school_10102016.csv'
part_by_school_df = pd.read_csv(part_by_school_path, encoding = "ISO-8859-1")

#full_school_data['entity_id'] = full_school_data['entity_id'].apply(lambda x: pd.to_numeric(x, errors='coerce'))

full_school_with_part = school_demogs.merge(part_by_school_df, how = 'left', on=['entity_id', 'school_year'])

del full_school_with_part['Unnamed: 0']


list_to_fill = ['hispanic','amer_indian','black','white','asian','pac_islander','multi_racial','total_minority','frl','ell','spec_ed', 'num_core_offering_participants', 'num_cum_core_offering_participants', 'num_offering_participants', 'num_cum_offering_participants', 'num_more_than_one_core_offering_participants']

for col in list_to_fill:
	full_school_with_part[col] = full_school_with_part[col].fillna(0)


full_school_with_part.to_csv('C:\\Users\KLA\Dropbox\MHC OPS Absent Narratives Approach\Evaluation (All) 2016-2017\Data\School master data\\working data\\schools_demogs_staff_participants_' + date + '.csv')

school_df = full_school_with_part

##creating columns for participation in offering percentages and demographic percentages

list_to_numeric = ['total_enroll','projected_enroll','hispanic','amer_indian','black','white','asian','pac_islander','multi_racial','total_minority','frl','ell','spec_ed','gifted','suspend_num']

for col in list_to_numeric:
	school_df[col] = school_df[col].apply(lambda x: pd.to_numeric(x, errors = 'coerce'))

##we could prob do this with some more for loops...

school_df['percent_core_offering'] = school_df['num_core_offering_participants'] / school_df['staff_count']
school_df['percent_cum_core_offering'] = school_df['num_cum_core_offering_participants'] / school_df['staff_count']
school_df['percent_offering'] = school_df['num_offering_participants'] / school_df['staff_count']
school_df['percent_cum_offering'] = school_df['num_cum_offering_participants'] / school_df['staff_count']
school_df['percent_more_than_one_core_offering'] = school_df['num_more_than_one_core_offering_participants'] / school_df['staff_count']

school_df['percent_amer_indian_stud'] = school_df['amer_indian'] / school_df['total_enroll']
school_df['percent_asian_stud'] = school_df['asian'] / school_df['total_enroll']
school_df['percent_black_stud'] = school_df['black'] / school_df['total_enroll']
school_df['percent_ell_stud'] = school_df['ell'] / school_df['total_enroll']
school_df['percent_frl_stud'] = school_df['frl'] / school_df['total_enroll']
school_df['percent_gifted_stud'] = school_df['gifted'] / school_df['total_enroll']
school_df['percent_hispanic_stud'] = school_df['hispanic'] / school_df['total_enroll']
school_df['percent_multi_racial_stud'] = school_df['multi_racial'] / school_df['total_enroll']
school_df['percent_pac_islander_stud'] = school_df['pac_islander'] / school_df['total_enroll']
school_df['percent_spec_ed_stud'] = school_df['spec_ed'] / school_df['total_enroll']
school_df['percent_minority_stud'] = school_df['total_minority'] / school_df['total_enroll']
school_df['percent_white_stud'] = school_df['white'] / school_df['total_enroll']
school_df['percent_suspend_stud'] = school_df['suspend_num'] / school_df['total_enroll']


#school_df = school_df.merge(entity_df, how='left', on = 'entity_id')

##THIS IS MASTER SCHOOL DATA SET
school_df.to_csv('C:\\Users\KLA\Dropbox\MHC OPS Absent Narratives Approach\Evaluation (All) 2016-2017\Data\School master data\\working data\\schools_demogs_staff_participants_percents_' + date + '.csv')
