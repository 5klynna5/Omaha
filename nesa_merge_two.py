import pandas as pd
print(pd.__version__)
import datetime as dt     
date = dt.datetime.today().strftime("%m%d%Y")

##read in existing master school data

school_path = 'C:\\Users\\KLA\\Dropbox\\MHC OPS Absent Narratives Approach\\Evaluation (All) 2016-2017\\Data\\School master data\\frozen data\\schools_master_data_11012016.csv'
school_df = pd.read_csv(school_path, encoding = "ISO-8859-1" )


del school_df['Unnamed: 0']

###read in nesa_data

nesa_path = 'C:\\Users\\KLA\\Dropbox\\MHC OPS Absent Narratives Approach\\Evaluation (All) 2016-2017\\Data\\NESA data\\frozen data\\nesa_entities_wide_formatted_11022016.csv'
nesa_df = pd.read_csv(nesa_path, encoding = "ISO-8859-1")

del nesa_df['Unnamed: 0']
##merge data sets together, left means that we are taking each rows in the school_df, and finding matching nesa rows

school_df = school_df.merge(nesa_df, how = 'outer', on=['entity_id', 'school_year'])

del school_df['Unnamed: 0.1']

entity_path = 'C:\\Users\\KLA\\Dropbox\\MHC OPS Absent Narratives Approach\\Evaluation (All) 2016-2017\\Data\\School master data\\working data\\entity_codebook_fall_data.csv'
entity_df = pd.read_csv(entity_path, encoding = "ISO-8859-1")

school_df = school_df.merge(entity_df, how = 'left', on = 'entity_id')

del school_df['entity_parent']
del school_df['entity_x']
del school_df['school']

school_df = school_df.rename(columns = {'entity_y': 'entity' })

eleven_cols = [col for col in school_df.columns if '11' in col]
eight_cols = [col for col in school_df.columns if '8' in col]
seven_cols = [col for col in school_df.columns if '7' in col]
six_cols = [col for col in school_df.columns if '6' in col]
five_cols = [col for col in school_df.columns if '5' in col]
four_cols = [col for col in school_df.columns if '4' in col]
three_cols = [col for col in school_df.columns if '3' in col]

nesa_cols = eleven_cols + eight_cols + seven_cols + six_cols + five_cols + four_cols + three_cols
nesa_list_cols = [eleven_cols, eight_cols, seven_cols, six_cols, five_cols, four_cols, three_cols]

non_nesa = [col for col in school_df.columns if col not in nesa_cols]
print(len(non_nesa))

numbers_list = ['eleven', 'eight', 'seven', 'six', 'five', 'four', 'three']

for item in nesa_list_cols:
	name = 'nesa_' + item[1].split('_')[1]
	columns = non_nesa + item
	df = school_df[columns]
	df = df.dropna(subset = [item], how = 'all')
	df.to_csv('C:\\Users\\KLA\\Dropbox\\MHC OPS Absent Narratives Approach\\Evaluation (All) 2016-2017\\Data\\NESA data\\working data\\wide format files\\' + name + '.csv')

#print(nesa_11_df.head())
#print(five.head())



##THIS IS MASTER SCHOOL DATA SET WITH NESA
#school_df.to_csv('C:\\Users\\KLA\\Dropbox\\MHC OPS Absent Narratives Approach\\Evaluation (All) 2016-2017\\Data\\NESA data\\working data\\schools_master_data_nesa' + date + '.csv')
