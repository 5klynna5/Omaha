import pandas as pd
print(pd.__version__)
import datetime as dt     
date = dt.datetime.today().strftime("%m%d%Y")

address_path = 'C:\\Users\\KLA\\Dropbox\\MHC OPS Absent Narratives Approach\\Evaluation (all) 2017-2018\\2017-2018 Data\\School Addresses\\ELSI_export_OPS_school_contact_info_2014_2015_11152017.csv'
address = pd.read_csv(address_path, encoding = "ISO-8859-1")

entity_path = 'C:\\Users\\KLA\\Dropbox\\MHC OPS Absent Narratives Approach\\Evaluation (all) 2017-2018\\2017-2018 Data\\entity_id_codebook.csv'
entity = pd.read_csv(entity_path, encoding  = "ISO-8859-1")

entity_address = entity.merge(address, how = 'left', on  = 'entity')

entity_address.to_csv('C:\\Users\\KLA\\Dropbox\\MHC OPS Absent Narratives Approach\\Evaluation (all) 2017-2018\\2017-2018 Data\\entity_id_addresses_fa17.csv')