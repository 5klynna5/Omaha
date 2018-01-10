import pandas as pd
print(pd.__version__)
import datetime as dt     
date = dt.datetime.today().strftime("%m%d%Y")


participation_path = 'C:\\Users\\KLA\\Dropbox\\MHC OPS Absent Narratives Approach\\Evaluation (all) 2017-2018\\2017-2018 Data\\Participation Data\\frozen_data\\cohort_not_cohort_attended_08142017.csv'
participation_data = pd.read_csv(participation_path, encoding = "ISO-8859-1")


###separate out data from each school year
data_13_14 = participation_data.loc[participation_data['school_year'] =='2013-2014']
data_14_15 = participation_data.loc[participation_data['school_year'] =='2014-2015']
data_15_16 = participation_data.loc[participation_data['school_year'] =='2015-2016']
data_16_17 = participation_data.loc[participation_data['school_year'] =='2016-2017']


'''
###this is total unique participants per school for each school year
schools_participants_13_14 = data_13_14.groupby('entity_id').person_id.nunique().to_frame().reset_index()
schools_participants_13_14.columns = ['entity_id', 'number_13_14']

schools_participants_14_15 = data_14_15.groupby('entity_id').person_id.nunique().to_frame().reset_index()
schools_participants_14_15.columns = ['entity_id', 'number_14_15']

schools_participants_15_16 = data_15_16.groupby('entity_id').person_id.nunique().to_frame().reset_index()
schools_participants_15_16.columns = ['entity_id', 'number_15_16']

schools_participants_16_17 = data_16_17.groupby('entity_id').person_id.nunique().to_frame().reset_index()
schools_participants_16_17.columns = ['entity_id', 'number_16_17']

schools_participants_total = participation_data.groupby('entity_id').person_id.nunique().to_frame().reset_index()
schools_participants_total.columns = ['entity_id', 'number_total_unique']
###merging together school years into one data frame

yrs_data = pd.merge(schools_participants_13_14, schools_participants_14_15, on='entity_id', how = 'outer')
yrs_data = pd.merge(yrs_data, schools_participants_15_16, on='entity_id', how = 'outer')
yrs_data = pd.merge(yrs_data, schools_participants_16_17, on='entity_id', how = 'outer')
yrs_data = pd.merge(yrs_data, schools_participants_total, on = 'entity_id', how = 'outer')

yrs_data = yrs_data.fillna(0)


yrs_data.to_csv('C:\\Users\KLA\Dropbox\MHC OPS Absent Narratives Approach\Evaluation (all) 2017-2018\\2017-2018 Data\Participation Data\working_data\\school_part_yrs_data_request_' + date + '.csv')

###merge in school name and addresses and lat long

school_address_data_path = 'C:\\Users\\KLA\\Dropbox\\MHC OPS Absent Narratives Approach\\Evaluation (all) 2017-2018\\2017-2018 Data\\School Addresses\\entity_id_addresses_fa17.csv'
school_address_data = pd.read_csv(school_address_data_path, encoding  = "ISO-8859-1")

yrs_data_addresses = pd.merge(school_address_data, yrs_data, on = 'entity_id', how = 'outer')

yrs_data_addresses = yrs_data_addresses.fillna(0)

yrs_data_addresses.to_csv('C:\\Users\\KLA\\Dropbox\\MHC OPS Absent Narratives Approach\\Evaluation (all) 2017-2018\\2017-2018 Data\\Participation Data\\working_data\\school_part_yrs_geo_' + date + '.csv')
'''