import pandas as pd
print(pd.__version__)
import datetime as dt     
date = dt.datetime.today().strftime("%m%d%Y")

staff_nums_path = 'C:\\Users\\KLA\\Dropbox\\MHC OPS Absent Narratives Approach\\Evaluation (all) 2017-2018\\2017-2018 Data\\Staff counts\\frozen data\\2016-ops-payroll-data_staff_counts_12122017.csv'
staff_nums = pd.read_csv(staff_nums_path, encoding = "ISO-8859-1")

school_events_path = 'C:\\Users\\KLA\\Dropbox\\MHC OPS Absent Narratives Approach\\Evaluation (all) 2017-2018\\2017-2018 Data\\Participation Data\\School Based Events\\frozen data\\school_based_events_from_part_fa16_calendar_fa16_to_fa17.csv'
school_events = pd.read_csv(school_events_path, encoding = "ISO-8859-1")

events_staff_nums = pd.merge(school_events, staff_nums, on = 'entity_id', how = 'left')
events_staff_nums.to_csv('C:\\Users\\KLA\\Dropbox\\MHC OPS Absent Narratives Approach\\Evaluation (all) 2017-2018\\2017-2018 Data\\Participation Data\\School Based Events\\frozen data\\events_part_fa16_calendar_fa16_to_fa17_staff_nums_' + date + '.csv')