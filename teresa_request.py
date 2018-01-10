import pandas as pd
print(pd.__version__)
import datetime as dt     
date = dt.datetime.today().strftime("%m%d%Y")

participation_path = 'C:\\Users\KLA\Dropbox\MHC OPS Absent Narratives Approach\Evaluation (All) 2016-2017\Data\Participation data\\frozen data\\cohort_not_cohort_attended_04182017.csv'
participation_data = pd.read_csv(participation_path, encoding = "ISO-8859-1")

###this is total unique participants per school over all time
schools_participants = participation_data.groupby('entity').person_id.nunique().to_frame().reset_index()
schools_participants.columns = ['entity', 'number_participants_all_time']
print(schools_participants.head())

#this is total participations per school over all time
schools_participations = participation_data.groupby('entity').number.sum().to_frame().reset_index()
schools_participations.columns = ['entity', 'number_participations_all_time']

#create data frame with just 2015-2016 and 2016-2017
new_data = participation_data.loc[participation_data['school_year'].isin(['2015-2016', '2016-2017'])]

new_schools_participants = new_data.groupby('entity').person_id.nunique().to_frame().reset_index()
new_schools_participants.columns = ['entity', 'number_participants_since_fa15']

new_schools_participations = new_data.groupby('entity').number.sum().to_frame().reset_index()
new_schools_participations.columns = ['entity', 'number_participations_since_fa15']

teresa_data = pd.merge(schools_participants, schools_participations, on = 'entity', how = 'outer')
teresa_data = pd.merge(teresa_data, new_schools_participants, on = 'entity', how = 'outer')
teresa_data = pd.merge(teresa_data, new_schools_participations, on = 'entity', how = 'outer')

teresa_data.to_csv('C:\\Users\\KLA\\Dropbox\\MHC OPS Absent Narratives Approach\\Evaluation (All) 2016-2017\\Data\\Participation Data\\working data\\teresa_data_request_04182017.csv')