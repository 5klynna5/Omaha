import pandas as pd
print(pd.__version__)
import datetime as dt     
date = dt.datetime.today().strftime("%m%d%Y")

partner_path = 'C:\\Users\\KLA\\Dropbox\\MHC OPS Absent Narratives Approach\\Evaluation (All) 2016-2017\\Data\\School master data\\frozen data\\partner_status_entities_2012_2017_.csv'
partner_df = pd.read_csv(partner_path, encoding = "ISO-8859-1" )

del partner_df['Unnamed: 0']

partner_df = partner_df.loc[partner_df['school_year'].isin(['2012-2013', '2013-2014', '2014-2015', '2015-2016'])]

partner_df['partner_num'] = partner_df['partner_status'].replace({'NON': 0, 'PARTNER': 1}).astype(float)


partner_cum_df = partner_df.groupby(by=['entity_id','school_year']).sum().groupby(level=[0]).cumsum()

partner_cum_df.to_csv('C:\\Users\\KLA\\Dropbox\\MHC OPS Absent Narratives Approach\\Evaluation (All) 2016-2017\\Data\\Partner School\\partner_cumulative_2012-2016.csv')

####merge into master data set

partner_cum_df = pd.read_csv('C:\\Users\\KLA\\Dropbox\\MHC OPS Absent Narratives Approach\\Evaluation (All) 2016-2017\\Data\\Partner School\\partner_cumulative_2012-2016.csv', encoding = "ISO-8859-1")

#school_df = pd.read_csv ('C:\\Users\\KLA\\Dropbox\\MHC OPS Absent Narratives Approach\\Evaluation (All) 2016-2017\\Data\\School master data\\frozen data\\schools_master_data_10262016.csv')
del partner_df['partner_num']

partner_df = partner_df.merge(partner_cum_df, how = 'outer', on=['entity_id', 'school_year'])


partner_df.to_csv('C:\\Users\\KLA\\Dropbox\\MHC OPS Absent Narratives Approach\\Evaluation (All) 2016-2017\\Data\\Partner School\\partner_master_data_' + date + '.csv')