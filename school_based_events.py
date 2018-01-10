import pandas as pd
print(pd.__version__)
import datetime as dt     
date = dt.datetime.today().strftime("%m%d%Y")

participation_path = 'C:\\Users\\KLA\\Dropbox\\MHC OPS Absent Narratives Approach\\Evaluation (all) 2017-2018\\2017-2018 Data\\Participation Data\\frozen_data\\mhc-ops_participation_all_to_06302017.csv'
participation_data = pd.read_csv(participation_path, encoding = "ISO-8859-1")

#len(participation_data)) 15443

ops_participation_data = participation_data.loc[participation_data['entity_parent'] == 'OPS']

#len(ops_participation_data)) 14392


attended_data = ops_participation_data.loc[ops_participation_data['attended'].isin(['Yes','YES'])]

school_based_data = attended_data.loc[attended_data['event_target'].isin(['SCHOOL_STUDENTS','SCHOOL_STAFF', 'SCHOOL_PARENTS'])]

school_based_data  = school_based_data.drop_duplicates(subset = ['program_id'])

school_based_data['source'] = 'PARTICIPATION'
print(school_based_data.head())


school_events_path = 'C:\\Users\KLA\Dropbox\MHC OPS Absent Narratives Approach\Evaluation (All) 2016-2017\Data\Events data\working data\\'
school_events_data = pd.read_csv(school_events_path + 'school_based_events_10202016.csv', encoding = "ISO-8859-1")

print(school_events_data.head())

school_events_all = pd.concat([school_events_data, school_based_data], join='inner', ignore_index=True, copy=False)


school_events_all.to_csv('C:\\Users\\KLA\\Dropbox\\MHC OPS Absent Narratives Approach\\Evaluation (all) 2017-2018\\2017-2018 Data\\Participation Data\\working_data\\school_based_events_merged_' + date + '.csv')

