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


###this is total unique participants per school for each school year
schools_participants_13_14 = data_13_14.groupby('entity').person_id.nunique().to_frame().reset_index()
schools_participants_13_14.columns = ['entity', 'number_13_14']

schools_participants_14_15 = data_14_15.groupby('entity').person_id.nunique().to_frame().reset_index()
schools_participants_14_15.columns = ['entity', 'number_14_15']

schools_participants_15_16 = data_15_16.groupby('entity').person_id.nunique().to_frame().reset_index()
schools_participants_15_16.columns = ['entity', 'number_15_16']

schools_participants_16_17 = data_16_17.groupby('entity').person_id.nunique().to_frame().reset_index()
schools_participants_16_17.columns = ['entity', 'number_16_17']

###merging together school years into one data frame

janet_yrs_data = pd.merge(schools_participants_13_14, schools_participants_14_15, on='entity', how = 'outer')
janet_yrs_data = pd.merge(janet_yrs_data, schools_participants_15_16, on='entity', how = 'outer')
janet_yrs_data = pd.merge(janet_yrs_data, schools_participants_16_17, on='entity', how = 'outer')

janet_yrs_data = janet_yrs_data.fillna(0)


janet_yrs_data.to_csv('C:\\Users\KLA\Dropbox\MHC OPS Absent Narratives Approach\Evaluation (all) 2017-2018\\2017-2018 Data\Participation Data\working_data\\janet_yrs_data_request_' + date + '.csv')

#####creating offering data frame over all time

janet_offerings_request = pd.pivot_table(participation_data,index=["entity"],values=["person_id"],
               columns=["offering_type"],aggfunc= pd.Series.nunique)

print(janet_offerings_request.head())

janet_offerings_request = janet_offerings_request.fillna(0)

partner_path = 'C:\\Users\\KLA\\Dropbox\\MHC OPS Absent Narratives Approach\\Evaluation (all) 2017-2018\\2017-2018 Data\\Participation Data\\working_data\\partner_and_focus_schools_17_18.csv'
partner_data = pd.read_csv(partner_path, encoding = "ISO-8859-1")

janet_offerings_request = pd.merge(janet_offerings_request, partner_path, on = 'entity', how = 'outer')


janet_offerings_request.to_csv('C:\\Users\KLA\Dropbox\MHC OPS Absent Narratives Approach\Evaluation (all) 2017-2018\\2017-2018 Data\Participation Data\working_data\\janet_offerings_data_request_' + date + '.csv')



