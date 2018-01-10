import pandas as pd
print(pd.__version__)
import datetime as dt     
date = dt.datetime.today().strftime("%m%d%Y")


master_path = 'C:\\Users\KLA\Dropbox\MHC OPS Absent Narratives Approach\Evaluation (All) 2016-2017\Data\School master data\\frozen data\\schools_master_data_12092016.csv'

partner_yrs_path = 'C:\\Users\KLA\Dropbox\MHC OPS Absent Narratives Approach\Evaluation (All) 2016-2017\Data\Partner School\\partner_status_2012_2017_num_years.csv'

master_df = pd.read_csv(master_path)

partner_yrs_df = pd.read_csv(partner_yrs_path)

print(partner_yrs_df.head())
print(master_df.head())

del partner_yrs_df['entity']

master_df = master_df.merge(partner_yrs_df, how = 'left', on = 'entity_id')

master_df['num_years_partner_total'].fillna(0, inplace=True)

del master_df['Unnamed: 0']

master_df.to_csv('C:\\Users\KLA\Dropbox\MHC OPS Absent Narratives Approach\Evaluation (All) 2016-2017\Data\School master data\\working data\\schools_master_data_' + date + '.csv')