import pandas as pd
print(pd.__version__)
import datetime as dt     
date = dt.datetime.today().strftime("%m%d%Y")

import numpy as np


participation_path = 'C:\\Users\KLA\Dropbox\MHC OPS Absent Narratives Approach\Evaluation (All) 2016-2017\Data\Participation data\\frozen data\\mhc-ops_participation_all_to_20161215_CREATED_03022017.csv'
participation_data = pd.read_csv(participation_path, encoding = "ISO-8859-1")

#len(participation_data)) 15443

ops_participation_data = participation_data.loc[participation_data['entity_parent'] == 'OPS']

#len(ops_participation_data)) 14392


attended_data = ops_participation_data.loc[ops_participation_data['attended'].isin(['Yes','YES'])]
##careful the yeses are not consistent here, some all caps

#len(attended_data)) 11740

attended_data['number'] = 1

##creating dataframe just for cohorts, must have attended two sessions to count as cohort participant after 2013, just count cohort entry before then

cohort_df = attended_data.loc[attended_data['event_type'] == 'COHORT']
cohort_df = cohort_df[['person_id', 'full_name', 'position', 'entity_id', 'entity', 'offering_type', 'program_id', 'event_type', 'semester', 'school_year', 'number', 'start_date', 'end_date']]

#len(cohort_df)) 498

cohort_session_df = attended_data.loc[attended_data['event_type'] == 'COHORT SESSION']
cohort_session_df = cohort_session_df[['person_id', 'full_name', 'position', 'entity_id', 'entity', 'offering_type', 'program_id', 'event_type', 'semester', 'school_year', 'number', 'start_date', 'end_date']]

#create a column to check if rows are duplicated (to check for more than one session attendance by same person)
cohort_session_df['duplicated'] = cohort_session_df.duplicated(['person_id', 'offering_type', 'semester', 'school_year'])

#len(cohort_session_df)) 7714

#create a dataframe of only those who had attended more than one cohort session for the cohort
cohort_multi_session_df = cohort_session_df.loc[cohort_session_df['duplicated'] == True]

#len(cohort_multi_session_df)) 5710

#combine old cohort entries with new cohort session entries where someone had attended more than one
cohort_df = pd.concat([cohort_df,cohort_multi_session_df])

#len(cohort_df)) 6208

cohort_df = cohort_df.drop_duplicates(['person_id', 'offering_type', 'semester', 'school_year'])

cohort_df = cohort_df.replace(to_replace ='COHORT SESSION', value = 'COHORT')
del cohort_df['duplicated']

#len(cohort_df)) 2272

cohort_df.to_csv('C:\\Users\KLA\Dropbox\MHC OPS Absent Narratives Approach\Evaluation (All) 2016-2017\Data\School master data\working data\cohort_attended_' + date + '.csv')

##creating full data set of cohort and not cohort offering participants
not_cohort_df = attended_data[attended_data['event_type'].isin(['COHORT','COHORT SESSION'])==False]
not_cohort_df = not_cohort_df[['person_id', 'full_name', 'position', 'entity_id', 'entity', 'offering_type', 'program_id', 'event_type', 'semester', 'school_year', 'number', 'start_date', 'end_date']]

#len(not_cohort_df)) 3528

attended_data = pd.concat([not_cohort_df, cohort_df])


#len(attended_data)) 5800
#so we have a total of 5800 offering participations, with each cohort being only counted once

attended_data.to_csv('C:\\Users\KLA\Dropbox\MHC OPS Absent Narratives Approach\Evaluation (All) 2016-2017\Data\Participation data\working data\cohort_not_cohort_attended_' + date + '.csv')
'''
attended_df_agg = attended_data[['person_id', 'full_name', 'position', 'entity_id', 'entity', 'school_year', 'number']]

attended_df_agg['entity_id'] = attended_df_agg['entity_id'].astype(str)
attended_df_agg['person_id'] = attended_df_agg['person_id'].astype(str)


attended_count = attended_df_agg.groupby(['entity_id','entity','school_year','person_id','full_name'], as_index=False).sum()

attended_count.to_csv('C:\\Users\KLA\Dropbox\MHC OPS Absent Narratives Approach\Evaluation (All) 2016-2017\Data\School master data\working data\offerings_count_by_school_' + date + '.csv')

#(len(attended_count)) 3121
attended_school = attended_count[['entity_id', 'school_year', 'person_id']]
attended_count_by_school = attended_school.groupby(['entity_id','school_year'], as_index=False).count()
attended_count_by_school['num_offering_participants'] = attended_count_by_school['person_id']
del attended_count_by_school['person_id']

#len(attended_count_by_school)) 297

#creates dataframe that counts cumulative participation at each year
#cumulative participation adds number of people participating that year and all previous years
###people can be counted again in each year

#this actually exports format we want, even though does not print the right way
attended_cum_df = attended_count_by_school.groupby(by=['entity_id','school_year']).sum().groupby(level=[0]).cumsum()

#len(attended_cum_df)) 297
##but then I have to reimport for it to be right format to merge?
attended_cum_df_path = 'C:\\Users\KLA\Dropbox\MHC OPS Absent Narratives Approach\Evaluation (All) 2016-2017\Data\School master data\working data\offerings_cum_by_school_' + date + '.csv'

attended_cum_df.to_csv(attended_cum_df_path)
attended_cum_df = pd.read_csv(attended_cum_df_path, encoding = "ISO-8859-1")

##apparently have to convert entity_ids to string to merge??
attended_cum_df['entity_id'] = attended_cum_df['entity_id'].astype(str)
#attended_cum_df['person_id'] = attended_cum_df['person_id'].astype(str)
attended_count_by_school['entity_id'] = attended_count_by_school['entity_id'].astype(str)
#attended_count_by_school['person_id'] = attended_count_by_school['person_id'].astype(str)


#outer merge means that we get all rows from each dataframe

attended_count_by_school = attended_count_by_school.merge(attended_cum_df, how='outer', on=['entity_id', 'school_year'])

#len(attended_count_by_school)) 297

attended_count_by_school.to_csv('C:\\Users\KLA\Dropbox\MHC OPS Absent Narratives Approach\Evaluation (All) 2016-2017\Data\School master data\working data\offerings_cum_and_count_by_school_' + date + '.csv')

##creating data frame of core offerings only - IC, SMS, RC, ISETAN, IMMERSION
core_df = attended_data.loc[attended_data['offering_type'].isin(['IC1', 'IC2', 'ISE', 'RC1', 'RC2', 'RC CLASSROOM/TEACHING EXPERIENCE', 'RC THEORY TO PRAXIS', 'RC WHOLE SCHOOL', 'SMS'])]

##creating data frame of all core offering participations, dropping column that specifies which one
core_df_agg = core_df[['person_id', 'full_name', 'position', 'entity_id', 'entity', 'school_year', 'number']]


core_df_agg['entity_id'] = core_df_agg['entity_id'].astype(str)
core_df_agg['person_id'] = core_df_agg['person_id'].astype(str)

#len(core_df_agg)) 2754
##so essentially, we've got 2272 cohort core offering participations, and 482 one day core offerings participations

##creating data frame that sums together all participations of each person
core_count = core_df_agg.groupby(['entity_id','entity','school_year','person_id','full_name'], as_index=False).sum()

#len(core_count)) 1786
#so about 1000 (more than a third) people took more than one offering in a school year

core_count.to_csv('C:\\Users\KLA\Dropbox\MHC OPS Absent Narratives Approach\Evaluation (All) 2016-2017\Data\School master data\working data\core_offerings_counts_' + date + '.csv')

##creating data frame of only those people who did more than one core offering in a school year
core_count_more_than_one = core_count.loc[core_count['number'] > 1]
core_count_more_than_one = core_count_more_than_one[['entity_id', 'school_year', 'person_id']]
core_more_than_one = core_count_more_than_one.groupby(['entity_id','school_year'], as_index=False).count()
core_more_than_one['num_more_than_one_core_offering_participants'] = core_more_than_one['person_id']
del core_more_than_one['person_id']

core_more_than_one['entity_id'] = core_more_than_one['entity_id'].astype(str)

#len(core_more_than_one)) 162

#creating data frame that counts each person at a school who has participated in at least one core offering
core_school = core_count[['entity_id', 'school_year', 'person_id']]
core_count_by_school = core_school.groupby(['entity_id','school_year'], as_index=False).count()
core_count_by_school['num_core_offering_participants'] = core_count_by_school['person_id']
del core_count_by_school['person_id']

#len(core_count_by_school)) 239

#creates dataframe that counts cumulative participation at each year
#this actually exports format we want, even though does not print the right way
core_cum_df = core_count_by_school.groupby(by=['entity_id','school_year']).sum().groupby(level=[0]).cumsum()

#len(core_cum_df)) 239

##but then I have to reimport for it to be right format to merge?
core_cum_df_path = 'C:\\Users\KLA\Dropbox\MHC OPS Absent Narratives Approach\Evaluation (All) 2016-2017\Data\School master data\working data\core_offerings_cum_by_school_' + date + '.csv'

core_cum_df.to_csv(core_cum_df_path)
core_cum_df = pd.read_csv(core_cum_df_path, encoding = "ISO-8859-1")

core_cum_df['num_cum_core_offering_participants'] = core_cum_df['num_core_offering_participants']
del core_cum_df['num_core_offering_participants']

core_cum_df['entity_id'] = core_cum_df['entity_id'].astype(str)
core_count_by_school['entity_id'] = core_count_by_school['entity_id'].astype(str)


core_count_by_school = core_count_by_school.merge(core_cum_df, how = 'outer', on=['entity_id', 'school_year'])

#len(core_count_by_school)) 239

core_count_by_school.to_csv('C:\\Users\KLA\Dropbox\MHC OPS Absent Narratives Approach\Evaluation (All) 2016-2017\Data\School master data\working data\core_offerings_count_by_school_' + date + '.csv')

##merging together dataframe which by school and school year has a column for:
#####num of core offering participants
#####num of cumulative core offering participants
#####num of total offering participants
#####num of cumulative total offering participants

all_and_core_by_school = attended_count_by_school.merge(core_count_by_school, how = 'outer', on = ['entity_id', 'school_year'])

##renaming columns appropriately
all_and_core_by_school['num_offering_participants'] = all_and_core_by_school['num_offering_participants_x']
all_and_core_by_school['num_cum_offering_participants'] = all_and_core_by_school['num_offering_participants_y']

del all_and_core_by_school['num_offering_participants_x']
del all_and_core_by_school['num_offering_participants_y']


all_and_core_by_school = all_and_core_by_school.merge(core_more_than_one, how='outer', on = ['entity_id', 'school_year'])

##replacing empty cells with 0
all_and_core_by_school.fillna(0, inplace=True)

#len(all_and_core_by_school)) 297
###so we did get all rows from attended data, sweet!

all_and_core_by_school.to_csv('C:\\Users\KLA\Dropbox\MHC OPS Absent Narratives Approach\Evaluation (All) 2016-2017\Data\School master data\working data\offerings_core_offerings_count_by_school_' + date + '.csv')
'''