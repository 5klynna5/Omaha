import pandas as pd
print(pd.__version__)
import datetime as dt     
date = dt.datetime.today().strftime("%m%d%Y")

##read in existing master school data

school_path = 'C:\\Users\\KLA\\Dropbox\\MHC OPS Absent Narratives Approach\\Evaluation (All) 2016-2017\\Data\\School master data\\frozen data\\schools_master_data_12092016.csv'
school_df = pd.read_csv(school_path, encoding = "ISO-8859-1" )


del school_df['Unnamed: 0']

###read in nesa_data

nesa_path = 'C:\\Users\\KLA\\Dropbox\\MHC OPS Absent Narratives Approach\\Evaluation (All) 2016-2017\\Data\\NESA data\\frozen data\\nesa_entities_wide_formatted_11022016.csv'
nesa_df = pd.read_csv(nesa_path, encoding = "ISO-8859-1")

del nesa_df['Unnamed: 0']
##merge data sets together, left means that we are taking each rows in the school_df, and finding matching nesa rows

school_df = school_df.merge(nesa_df, how = 'left', on=['entity_id', 'school_year'])


##THIS IS MASTER SCHOOL DATA SET WITH NESA
school_df.to_csv('C:\\Users\\KLA\\Dropbox\\MHC OPS Absent Narratives Approach\\Evaluation (All) 2016-2017\\Data\\NESA data\\working data\\schools_master_data_nesa' + date + '.csv')
