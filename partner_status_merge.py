import pandas as pd
print(pd.__version__)
import datetime as dt     
date = dt.datetime.today().strftime("%m%d%Y")

import os
import glob

entity_path = 'C:\\Users\\KLA\\Dropbox\\MHC OPS Absent Narratives Approach\\Evaluation (All) 2016-2017\\Data\\School master data\\working data\\entity_codebook_fall_data.csv'
entity_df = pd.read_csv(entity_path, encoding = "ISO-8859-1")


partner_path = 'C:\\Users\\KLA\\Dropbox\\MHC OPS Absent Narratives Approach\\Evaluation (All) 2016-2017\\Data\\Partner School\\partner_status_formatted_2012_2017.csv'
partner_df = pd.read_csv(partner_path, encoding = "ISO-8859-1")


del partner_df['Unnamed: 0']

entities_partners = partner_df.merge(entity_df, how='outer', on='entity_id')

print(entities_partners.head())

entities_partners['partner_status'].fillna('NON', inplace=True)


entities_partners.to_csv('C:\\Users\\KLA\\Dropbox\\MHC OPS Absent Narratives Approach\\Evaluation (All) 2016-2017\\Data\\Partner School\\partner_status_entities_' + date + '.csv')





