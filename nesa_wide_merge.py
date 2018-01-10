import pandas as pd
print(pd.__version__)
import datetime as dt     
date = dt.datetime.today().strftime("%m%d%Y")

school_path = 'C:\\Users\\KLA\\Dropbox\\MHC OPS Absent Narratives Approach\\Evaluation (All) 2016-2017\\Data\\School master data\\frozen data\\schools_master_data_wide_no_alt_01312017.csv'
school_df = pd.read_csv(school_path, encoding = "ISO-8859-1" )


nesa_totals_path = 'C:\\Users\\KLA\\Dropbox\\MHC OPS Absent Narratives Approach\\Evaluation (All) 2016-2017\\Data\\NESA data\\working data\\wide format files\\nesa_entities_totals_wide_01312017.csv'
nesa_totals_df = pd.read_csv(nesa_totals_path, encoding = "ISO-8859-1")


nesa_path = 'C:\\Users\\KLA\\Dropbox\\MHC OPS Absent Narratives Approach\\Evaluation (All) 2016-2017\Data\\School master data\\working data\\schools_master_data_nesa_wide_01312017.csv'
nesa_df = pd.read_csv(nesa_path, encoding = "ISO-8859-1")

school_df = school_df.merge(nesa_totals_df, on = 'entity_id', how='left')

school_df = school_df.merge(nesa_df, on='entity_id', how='left')

del school_df['Unnamed: 0']

school_df.to_csv('C:\\Users\\KLA\\Dropbox\\MHC OPS Absent Narratives Approach\\Evaluation (All) 2016-2017\\Data\\School master data\\frozen data\\schools_all_wide_' + date + '.csv')