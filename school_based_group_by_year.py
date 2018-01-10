import pandas as pd
print(pd.__version__)
import datetime as dt     
date = dt.datetime.today().strftime("%m%d%Y")

school_based_path = 'C:\\Users\KLA\Dropbox\MHC OPS Absent Narratives Approach\Evaluation (All) 2016-2017\Data\Events data\working data\\school_based_events_merged_deduped_10252016.csv'
school_based_data = pd.read_csv(school_based_path, encoding = "ISO-8859-1")

school_based_data['event_target'] = school_based_data['event_target'].apply(lambda x: x.upper())

school_based_data['number'] = 1

school_based_counts = school_based_data.groupby(['school_year', 'entity_id'], as_index=False).sum()

#del school_based_counts['Unnamed: 0']

school_events_cum_df = school_based_counts.groupby(by=['entity_id','school_year']).sum().groupby(level=[0]).cumsum()

school_events_cum_df.to_csv('C:\\Users\KLA\Dropbox\MHC OPS Absent Narratives Approach\Evaluation (All) 2016-2017\Data\School master data\working data\\school_based_events_cum_sum_' + date + '.csv')

school_events_cum_path = 'C:\\Users\KLA\Dropbox\MHC OPS Absent Narratives Approach\Evaluation (All) 2016-2017\Data\School master data\working data\\school_based_events_cum_sum_' + date + '.csv'
school_events_cum_df = pd.read_csv(school_events_cum_path, encoding = "ISO-8859-1")


school_based_counts = school_based_counts.merge(school_events_cum_df, how='right', on=['entity_id', 'school_year'])

school_based_counts = school_based_counts.rename(columns={'number_x': 'num_school_based_events', 'number_y': 'num_cum_school_based_events'})

school_based_counts.to_csv('C:\\Users\KLA\Dropbox\MHC OPS Absent Narratives Approach\Evaluation (All) 2016-2017\Data\School master data\working data\\school_based_events_num_and_cum_' + date + '.csv')