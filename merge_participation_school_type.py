import pandas as pd
print(pd.__version__)
import datetime as dt
import numpy as np     
date = dt.datetime.today().strftime("%m%d%Y")

part_path = 'C:\\Users\\KLA\\Dropbox\\MHC OPS Absent Narratives Approach\\Evaluation (All) 2016-2017\\Data\\Participation Data\\frozen data\\cohort_not_cohort_attended_03032017.csv'

participation = pd.read_csv(part_path, encoding = "ISO-8859-1")
participation['entity_id'] = pd.to_numeric(participation['entity_id'], errors='coerce')

type_path = 'C:\\Users\\KLA\\Dropbox\\MHC OPS Absent Narratives Approach\\Evaluation (All) 2016-2017\\Data\\ops_entities_school_type.csv'

school_type = pd.read_csv(type_path, encoding = "ISO-8859-1")
school_type['entity_id'] = pd.to_numeric(school_type['entity_id'], errors='coerce')

part_with_type = pd.merge(participation, school_type, on = 'entity_id', how='left')

print(part_with_type.head())

del part_with_type['Unnamed: 0']

partner_path = 'C:\\Users\\KLA\\Dropbox\\MHC OPS Absent Narratives Approach\\Evaluation (All) 2016-2017\\Data\\Partner School\\entities_partner_status_2016-2017.csv'
partner = pd.read_csv(partner_path, encoding = "ISO-8859-1")

partner['entity_id'] = pd.to_numeric(partner['entity_id'], errors='coerce')

part_with_type_partner = pd.merge(part_with_type, partner, on = 'entity_id', how = 'left')

part_with_type_partner.to_csv('C:\\Users\\KLA\\Dropbox\\MHC OPS Absent Narratives Approach\\Evaluation (All) 2016-2017\\Data\\Participation Data\\working data\\attended_data_school_type_partner' + date + '.csv')

