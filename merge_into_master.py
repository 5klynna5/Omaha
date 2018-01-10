import pandas as pd
print(pd.__version__)
import datetime as dt     
date = dt.datetime.today().strftime("%m%d%Y")

##read in existing master school data

school_path = 'C:\\Users\KLA\Dropbox\MHC OPS Absent Narratives Approach\Evaluation (All) 2016-2017\Data\School master data\working data\\schools_demogs_staff_participants_percents_11102016.csv'
school_df = pd.read_csv(school_path, encoding = "ISO-8859-1" )

del school_df['Unnamed: 0']

###read in data created using 'schoool_based_group_by_year.py' on how many events had happened at a school in each year, and cumulative

school_events_path = 'C:\\Users\KLA\Dropbox\MHC OPS Absent Narratives Approach\Evaluation (All) 2016-2017\Data\School master data\working data\\school_based_events_num_and_cum_10262016.csv'
school_events_count = pd.read_csv(school_events_path, encoding = "ISO-8859-1")

del school_events_count['Unnamed: 0']

##merge data sets together, left means that we are taking each rows in the school_df, and finding matching school events count. 

school_df = school_df.merge(school_events_count, how = 'left', on=['entity_id', 'school_year'])

#del school_df['Unnamed: 0']
school_df['num_school_based_events'].fillna(0, inplace=True)
school_df['num_cum_school_based_events'].fillna(0, inplace=True)


##read in partner status dataframe
partner_path = 'C:\\Users\\KLA\\Dropbox\\MHC OPS Absent Narratives Approach\\Evaluation (All) 2016-2017\\Data\\Partner School\\partner_master_data_11042016.csv'
partner_df = pd.read_csv(partner_path, encoding = "ISO-8859-1")

##delete columns that will mess up merge
del partner_df['Unnamed: 0']
del partner_df['entity']

##merge into master school data frame
school_df = school_df.merge(partner_df, how = 'left', on = ['entity_id', 'school_year'])

print(school_df.head())

##THIS IS MASTER SCHOOL DATA SET
school_df.to_csv('C:\\Users\KLA\Dropbox\MHC OPS Absent Narratives Approach\Evaluation (All) 2016-2017\Data\School master data\\working data\\schools_master_data_' + date + '.csv')
