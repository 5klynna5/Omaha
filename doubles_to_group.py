import pandas as pd
print(pd.__version__)
import datetime as dt     
date = dt.datetime.today().strftime("%m%d%Y")

path_behavior = 'C:\\Users\KLA\Dropbox\MHC OPS Absent Narratives Approach\Evaluation (All) 2016-2017\Data\School master data\working data\Official Fall Data (Demographics)\\suspend_mobility_attend_KA_doubles_11072016.csv'
behavior_df = pd.read_csv(path_behavior, encoding = "ISO-8859-1")

behavior_df = behavior_df[['school', 'school_year', 'suspend_num', 'mobility_num_calc', 'attend_num_calc', 'total_enroll']]

entity_df = pd.read_csv('C:\\Users\KLA\Dropbox\MHC OPS Absent Narratives Approach\Evaluation (All) 2016-2017\Data\School master data\\working data\\fall_data_entity_codebook.csv')

behavior_df = behavior_df.merge(entity_df, how = "left", on = ['school'])

print(behavior_df.head())

behavior_grouped = behavior_df.groupby(['school_year', 'entity', 'entity_id'], as_index=False).sum()

behavior_grouped.to_csv('C:\\Users\KLA\Dropbox\MHC OPS Absent Narratives Approach\Evaluation (All) 2016-2017\Data\School master data\working data\Official Fall Data (Demographics)\\suspend_mobility_attend_KA_doubles_grouped_' + date + '.csv')

