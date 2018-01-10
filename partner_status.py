import pandas as pd
print(pd.__version__)
import datetime as dt     
date = dt.datetime.today().strftime("%m%d%Y")

##load in partner status csv created from keith's file
path_partners = 'C:\\Users\\KLA\\Dropbox\\MHC OPS Absent Narratives Approach\\Evaluation (All) 2016-2017\\Data\\Partner School\\'
partners_df = pd.read_csv(path_partners + 'partner_status_2012_2017.csv', encoding = "ISO-8859-1")

entity_path = 'C:\\Users\\KLA\\Dropbox\\MHC OPS Absent Narratives Approach\\Evaluation (All) 2016-2017\\Data\\School master data\\working data\\entity_codebook_fall_data.csv'
entity_df = pd.read_csv(entity_path, encoding = "ISO-8859-1")


del partners_df['entity_partners']
del entity_df['entity_parent']

partners_df = pd.concat([partners_df, entity_df])

partners_df = partners_df.drop_duplicates(subset = 'entity_id')


partners_df = partners_df.fillna('NON')

##change from wide to long format, so that school year is one column, not multiple columns, to match master data set
partners_long = pd.melt(partners_df, id_vars=['entity_id'], value_vars=['2012-2013', '2013-2014', '2014-2015', '2015-2016', '2016-2017'])

##replacing variable names, keeping with all caps convention
partners_long = partners_long.replace(to_replace = ['Non-partner', 'Non-Partner', 'Partner'], value = ['NON', 'NON', 'PARTNER'])

##replacing column names to match master dat set
partners_long = partners_long.rename(columns={'variable': 'school_year', 'value': 'partner_status'})

partners_df = partners_long.merge(entity_df, how = 'left', on = 'entity_id')


##saving as a csv, properly formatted
partners_df.to_csv(path_partners + 'partner_status_entities_2012_2017_.csv')
