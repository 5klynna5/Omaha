import pandas as pd
print(pd.__version__)
import datetime as dt     
date = dt.datetime.today().strftime("%m%d%Y")


path = 'C:\\Users\KLA\Dropbox\MHC OPS Absent Narratives Approach\Evaluation (all) 2017-2018\\2017-2018 Data\Participation Data\\frozen_data\\cohort_not_cohort_attended_08142017.csv'
all_data = pd.read_csv(path, encoding = "ISO-8859-1")

partner_path = 'C:\\Users\KLA\Dropbox\MHC OPS Absent Narratives Approach\Evaluation (all) 2017-2018\\2017-2018 Data\Partner Schools Lists\\partner_schools_2017_2018.csv'
partner_data = pd.read_csv(partner_path, encoding = "ISO-8859-1")

partner_data['entity_id'] = pd.to_numeric(partner_data['entity_id'], errors = 'coerce')

del all_data['Unnamed: 0']

num_cols = ['entity_id', 'person_id', 'program_id']

string_cols = ['entity', 'event_type', 'full_name', 'offering_type', 'position', 'school_year', 'semester']

for col in string_cols:
	all_data[col] = all_data[col].str.rstrip(' ')

for col in num_cols:
	all_data[col] = pd.to_numeric(all_data[col], errors = 'coerce')

all_data['first_name'] = all_data['full_name'].apply(lambda x: pd.Series(x.split(' ')))[0]
all_data['last_name'] = all_data['full_name'].apply(lambda x: pd.Series(x.split(' ')))[1]
all_data['last_first_name'] = all_data['last_name'] + ', ' + all_data['first_name']

partner_ids = partner_data['entity_id'].tolist()

leadership_offerings = ['SAT', 'PRINCIPAL COHORT']

for entity_id in partner_ids:
	df = all_data.loc[all_data['entity_id'] == entity_id]
	df.to_csv('C:\\Users\KLA\Dropbox\MHC OPS Absent Narratives Approach\Evaluation (all) 2017-2018\\2017-2018 Data\Excel School Profiles\\records_by_entity\\' + str(entity_id) + '.csv')
	leaders_df = df.loc[df['offering_type'].isin(leadership_offerings)]
	leaders_df = leaders_df[['last_first_name', 'position', 'offering_type', 'school_year', 'semester', 'program_id']]
	leaders_df = leaders_df.pivot_table(index=['last_first_name', 'position', 'offering_type', 'school_year', 'semester'], aggfunc='count')
	leaders_df.to_csv('C:\\Users\KLA\Dropbox\MHC OPS Absent Narratives Approach\Evaluation (all) 2017-2018\\2017-2018 Data\Excel School Profiles\\records_by_entity\\' + str(entity_id) + '_leadership.csv')
	individuals_df = df.loc[~df['offering_type'].isin(leadership_offerings)]
	individuals_df = individuals_df[['school_year', 'last_first_name', 'position', 'offering_type', 'semester', 'program_id']]
	#individuals_df = individuals_df.pivot_table(index = ['school_year', 'last_first_name', 'position', 'offering_type', 'semester'], aggfunc = 'count')
	individuals_df = individuals_df.sort_values(by = ['school_year', 'last_first_name'], ascending = [0,1])
	individuals_df.to_csv('C:\\Users\KLA\Dropbox\MHC OPS Absent Narratives Approach\Evaluation (all) 2017-2018\\2017-2018 Data\Excel School Profiles\\records_by_entity\\' + str(entity_id) + '_individuals.csv')
