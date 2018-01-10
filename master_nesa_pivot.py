import pandas as pd
print(pd.__version__)
import datetime as dt     
date = dt.datetime.today().strftime("%m%d%Y")

school_path = 'C:\\Users\\KLA\\Dropbox\\MHC OPS Absent Narratives Approach\\Evaluation (All) 2016-2017\\Data\\School master data\\working data\\schools_master_data_nesa_12222016.csv'
school_df = pd.read_csv(school_path, encoding = "ISO-8859-1" )

del school_df['Unnamed: 0']
del school_df['Unnamed: 0.1']

wide_df = school_df.pivot(index='entity_id', columns='school_year')

print(list(wide_df.columns))

#wide_df.to_csv('C:\\Users\\KLA\\Dropbox\\MHC OPS Absent Narratives Approach\\Evaluation (All) 2016-2017\\Data\\School master data\\working data\\schools_master_data_nesa_wide_' + date + '.csv')

#wide_df_path = 'C:\\Users\\KLA\\Dropbox\\MHC OPS Absent Narratives Approach\\Evaluation (All) 2016-2017\\Data\\School master data\\working data\\schools_master_data_nesa_wide_12222016.csv'
#wide_df = pd.read_csv(wide_df_path, encoding = "ISO-8859-1" )

