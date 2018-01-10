import pandas as pd
print(pd.__version__)
import datetime as dt     
date = dt.datetime.today().strftime("%m%d%Y")

import numpy as np


participation_path = 'C:\\Users\KLA\Dropbox\MHC OPS Absent Narratives Approach\Evaluation (all) 2017-2018\\2017-2018 Data\Participation Data\\frozen_data\\mhc-ops_participation_all_to_06302017.csv'
participation_data = pd.read_csv(participation_path, encoding = "ISO-8859-1")

#print(len(participation_data))
#sp17 - 19807
#fa16 - 18088

##this trims white space from column names
participation_data = participation_data.rename(columns=lambda x: x.rstrip(" "))

print(participation_data.columns)

#this trims white space from this column
participation_data['entity_parent'] = participation_data['entity_parent'].astype(str).apply(lambda x: x.rstrip(" "))

ops_participation_data = participation_data[participation_data['entity_parent'] =='OPS']

#print(len(ops_participation_data)) 
#sp17 - 18583
#fa16 - 16917

ops_participation_data['attended'] = ops_participation_data['attended'].astype(str).apply(lambda x: x.rstrip(" "))

#this trims white space from this column
attended_data = ops_participation_data[ops_participation_data['attended'].isin(['Yes','YES','TRUE'])]
##careful the yeses are not consistent here, some all caps

#print(len(attended_data)) 
#sp17 - 14753
#fa16 - 13646


attended_data['number'] = 1


##creating dataframe just for cohorts, must have attended two sessions to count as cohort participant after 2013, just count cohort entry before then

attended_data['event_type'] = attended_data['event_type'].astype(str).apply(lambda x: x.rstrip(" "))
attended_data['event_type'] = attended_data['event_type'].apply(lambda x: x.upper())

cohort_df = attended_data[attended_data['event_type'] == 'COHORT']
cohort_df = cohort_df[['person_id', 'full_name', 'position', 'entity_id', 'entity', 'offering_type', 'program_id', 'event_type', 'semester', 'school_year', 'number', 'start_date', 'end_date']]

#print(len(cohort_df)) 
#sp17 - 498
#fa16 - 498

cohort_session_df = attended_data[attended_data['event_type'] == 'COHORT SESSION']
cohort_session_df = cohort_session_df[['person_id', 'full_name', 'position', 'entity_id', 'entity', 'offering_type', 'program_id', 'event_type', 'semester', 'school_year', 'number', 'start_date', 'end_date']]

#create a column to check if rows are duplicated (to check for more than one session attendance by same person)
cohort_session_df['duplicated'] = cohort_session_df.duplicated(['person_id', 'offering_type', 'semester', 'school_year'])

#print(len(cohort_session_df)) 
#sp17 - 9857
#fa16 - 8927

#create a dataframe of only those who had attended more than one cohort session for the cohort
cohort_multi_session_df = cohort_session_df.loc[cohort_session_df['duplicated'] == True]

#print(len(cohort_multi_session_df)) 
#sp17 - 7194
#fa16 - 6596

#combine old cohort entries with new cohort session entries where someone had attended more than one
cohort_df = pd.concat([cohort_df,cohort_multi_session_df])

print(len(cohort_df)) 
#sp17 - 7692
#fa16 - 7094

cohort_df = cohort_df.drop_duplicates(['person_id', 'offering_type', 'semester', 'school_year'])

cohort_df = cohort_df.replace(to_replace ='COHORT SESSION', value = 'COHORT')
del cohort_df['duplicated']

#print(len(cohort_df))
#sp17 - 2870
#fa16 - 2567

cohort_df.to_csv('C:\\Users\KLA\Dropbox\MHC OPS Absent Narratives Approach\Evaluation (all) 2017-2018\\2017-2018 Data\Participation Data\working_data\cohort_attended_' + date + '.csv')

##creating full data set of cohort and not cohort offering participants
not_cohort_df = attended_data[attended_data['event_type'].isin(['COHORT','COHORT SESSION'])==False]
not_cohort_df = not_cohort_df[['person_id', 'full_name', 'position', 'entity_id', 'entity', 'offering_type', 'program_id', 'event_type', 'semester', 'school_year', 'number', 'start_date', 'end_date']]

not_cohort_df.to_csv('C:\\Users\KLA\Dropbox\MHC OPS Absent Narratives Approach\Evaluation (all) 2017-2018\\2017-2018 Data\Participation Data\working_data\\not_cohort_attended_' + date + '.csv')
#print(len(not_cohort_df)) 
#sp17 - 4398
#fa16 - 4221

attended_data = pd.concat([not_cohort_df, cohort_df])

print(attended_data['school_year'].value_counts())

print(attended_data['offering_type'].value_counts())
#print(len(attended_data)) 
#sp17 - 7268
#fa16 - 6788
#so we have a total of 7268 offering participations including spring 2017, with each cohort being only counted once

print(attended_data.person_id.nunique())
#sp17 - 2535
#so we have a total of 2535 unique ops educators who have participated

attended_data.to_csv('C:\\Users\KLA\Dropbox\MHC OPS Absent Narratives Approach\Evaluation (all) 2017-2018\\2017-2018 Data\Participation Data\working_data\cohort_not_cohort_attended_' + date + '.csv')

