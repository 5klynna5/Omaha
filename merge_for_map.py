import pandas as pd
print(pd.__version__)
import datetime as dt     
date = dt.datetime.today().strftime("%m%d%Y")

####participation and address file
participation_path = 'C:\\Users\\KLA\\Dropbox\\MHC OPS Absent Narratives Approach\\Evaluation (all) 2017-2018\\2017-2018 Data\\School Addresses\\school_part_yrs_geo_11162017.csv'
participation_data = pd.read_csv(participation_path, encoding = "ISO-8859-1")

del participation_data['Unnamed: 0']

###partner school data spreadsheet
partner_path = 'C:\\Users\\KLA\\Dropbox\\MHC OPS Absent Narratives Approach\\Evaluation (all) 2017-2018\\2017-2018 Data\\Partner Schools Lists\\partner_schools_2017_2018.csv'
partner_data = pd.read_csv(partner_path, encoding = "ISO-8859-1")

del partner_data['entity_name']

###merge together spreadsheets
participation_data  = pd.merge(participation_data, partner_data, on = "entity_id", how = "left")

participation_data['partner_status_2017_2018'] = participation_data['partner_status_2017_2018'].fillna('NOT PARTNER')

participation_data.to_csv('C:\\Users\\KLA\\Dropbox\\MHC OPS Absent Narratives Approach\\Evaluation (all) 2017-2018\\2017-2018 Data\\School Addresses\\school_part_partner_addresses_' + date + '.csv')