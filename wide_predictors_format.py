import pandas as pd
print(pd.__version__)
import datetime as dt     
date = dt.datetime.today().strftime("%m%d%Y")

school_path = 'C:\\Users\\KLA\\Dropbox\\MHC OPS Absent Narratives Approach\\Evaluation (All) 2016-2017\\Data\\School master data\\frozen data\\'
school_file = 'schools_master_data_wide_no_alt_01302017.csv'
schools_df = pd.read_csv(school_path + school_file, encoding = "ISO-8859-1")


#schools_df = schools_df.replace(['NON',0], ['PARTNER',1])

print(schools_df.columns)

schools_df['suspend_percent_change_12_13_to_13_14'] = schools_df['percent_suspend_stud2013-2014'] - schools_df['percent_suspend_stud2012-2013']
schools_df['suspend_percent_change_13_14_to_14_15'] = schools_df['percent_suspend_stud2014-2015'] = schools_df['percent_suspend_stud2013-2014']

del schools_df['suspend_percent_change_12_13_to_14_15']


schools_df.to_csv('C:\\Users\\KLA\\Dropbox\\MHC OPS Absent Narratives Approach\\Evaluation (All) 2016-2017\\Data\\School master data\\frozen data\\schools_master_data_wide_'+ date+'.csv')