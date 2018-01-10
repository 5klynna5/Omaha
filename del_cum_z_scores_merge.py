import pandas as pd
print(pd.__version__)
import datetime as dt
import numpy as np     
date = dt.datetime.today().strftime("%m%d%Y")

data_path = 'C:\\Users\\KLA\\Dropbox\\MHC OPS Absent Narratives Approach\\Evaluation (All) 2016-2017\\Data\\School master data\\frozen data\\schools_all_wide_small_dropped_02152017.csv'
data = pd.read_csv(data_path, encoding  = "ISO-8859-1")


percent_cum_cols = [col for col in data.columns if 'percent_cum' in col]

print(percent_cum_cols)

data = data.drop(percent_cum_cols, axis=1)


z_scores_path = 'C:\\Users\\KLA\\Dropbox\\MHC OPS Absent Narratives Approach\\Evaluation (All) 2016-2017\\Data\\School master data\\frozen data\\schools_all_wide_01312017_zscores.csv'
z_scores = pd.read_csv(z_scores_path, encoding  = "ISO-8859-1")


z_list = ['_sd', '_var', '_z']

z_score_cols = [col for col in z_scores.columns if '_sd' in col] + [col for col in z_scores.columns if '_var' in col] + [col for col in z_scores.columns if '_wtmean' in col] + [col for col in z_scores.columns if '_z' in col]

z_score_cols.append('entity_id')


z_scores = z_scores[z_score_cols]


data = pd.merge(data, z_scores, how='left', on='entity_id' )

del data['Unnamed: 0']

print(data.columns)

data.to_csv('C:\\Users\\KLA\\Dropbox\\MHC OPS Absent Narratives Approach\\Evaluation (All) 2016-2017\\Data\\School master data\\frozen data\\schools_all_wide_small_dropped_02162017.csv')
