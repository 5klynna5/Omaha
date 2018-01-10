import pandas as pd
print(pd.__version__)
import datetime as dt     
date = dt.datetime.today().strftime("%m%d%Y")

import os
import glob

##load in the csvs with each school type's data
#check that its set right, use this script for totals and all demographics
directory = 'C:\\Users\\KLA\\Dropbox\\MHC OPS Absent Narratives Approach\\Evaluation (All) 2016-2017\\Data\\NESA data\\working data\\formatted files\\'

##concatenate all of the school types / grade levels into one data frame
allFiles = glob.glob(directory + "/*.csv")
nesa_df = pd.DataFrame()
list_ = []
for file_ in allFiles:
    df = pd.read_csv(file_, encoding = "ISO-8859-1")
    list_.append(df)
nesa_df = pd.concat(list_)


##replace the race categories used with the categories used in our other data
nesa_df['demographic_type'] = nesa_df['demographic_type'].replace(to_replace = ['esl', 'sped'], value = ['ell', 'spec_ed'])
nesa_df['demographic'] = nesa_df['demographic'].replace(to_replace=['AM','AS','BL','PI','HI','MU','WH'], value=['amer_indian', 'asian', 'black', 'pac_islander', 'hispanic', 'multi_racial', 'white'])

nesa_df.rename(columns = {'entity':'entity_nesa'}, inplace = True)

nesa_df['demographic_type'] = nesa_df['demographic_type'].astype(str).map(lambda x: x.upper())
nesa_df['subject'] = nesa_df['subject'].astype(str).map(lambda x: x.upper())


##load in entity codebook
nesa_entities = pd.read_csv('C:\\Users\\KLA\\Dropbox\\MHC OPS Absent Narratives Approach\\Evaluation (All) 2016-2017\\Data\\NESA data\\working data\\entity_codebook_fall_data_nesa.csv', encoding = "ISO-8859-1")

##merge entity ids in with the data set, merging on the names used in the nesa data set
nesa_entity_ids = nesa_df.merge(nesa_entities, how='left', on='entity_nesa')

del nesa_entity_ids['Unnamed: 0']
del nesa_entity_ids['entity_parent']


#save the dataframe to a csv
nesa_entity_ids.to_csv('C:\\Users\\KLA\\Dropbox\\MHC OPS Absent Narratives Approach\\Evaluation (All) 2016-2017\\Data\\NESA data\\working data\\nesa_with_entities_' + date +'.csv')
