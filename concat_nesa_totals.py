import pandas as pd
print(pd.__version__)
import datetime as dt     
date = dt.datetime.today().strftime("%m%d%Y")

import os
import glob


directory = 'C:\\Users\\KLA\\Dropbox\\MHC OPS Absent Narratives Approach\\Evaluation (All) 2016-2017\\Data\\NESA data\\working data\\totals files\\'

allFiles = glob.glob(directory + "/*.csv")
nesa_totals = pd.DataFrame()
list_ = []
for file_ in allFiles:
    df = pd.read_csv(file_, encoding = "ISO-8859-1")
    list_.append(df)
nesa_totals = pd.concat(list_)

del nesa_totals['Unnamed: 0']

nesa_totals['entity_nesa'] = nesa_totals['entity']

del nesa_totals['entity']

entities_path = 'C:\\Users\\KLA\\Dropbox\\MHC OPS Absent Narratives Approach\\Evaluation (All) 2016-2017\\Data\\NESA data\\working data\\entity_codebook_fall_data_nesa.csv'
entities = pd.read_csv(entities_path, encoding = "ISO-8859=1")

nesa_totals = nesa_totals.merge(entities, on='entity_nesa', how = 'left')

nesa_totals.drop(['Unnamed: 0.1', 'entity_id_x', 'entity_parent_x', 'entity_nesa', 'entity_parent_y'], axis = 1, inplace=True)

nesa_totals.to_csv(directory + 'nesa_totals_all_' + date + ".csv")