
import pandas as pd
print(pd.__version__)
import datetime as dt     
date = dt.datetime.today().strftime("%m%d%Y")


nesa_path = 'C:\\Users\\KLA\\Dropbox\\MHC OPS Absent Narratives Approach\\Evaluation (All) 2016-2017\\Data\\NESA data\\working data\\totals files\\nesa_totals_all_01312017.csv'

nesa_df = pd.read_csv(nesa_path, encoding = "ISO-8859-1")

nesa_df =  nesa_df[nesa_df.grade != 'ALL']

nesa_df_wide = pd.pivot_table(nesa_df, values='average_scale_score', index='entity_id', columns=['school_year', 'grade', 'subject'])


nesa_df_wide.to_csv('C:\\Users\\KLA\\Dropbox\\MHC OPS Absent Narratives Approach\\Evaluation (All) 2016-2017\\Data\\NESA data\\working data\\wide format files\\nesa_entities_totals_wide_' + date + '.csv')

'''
nesa_df_wide = pd.read_csv('C:\\Users\\KLA\\Dropbox\\MHC OPS Absent Narratives Approach\\Evaluation (All) 2016-2017\\Data\\NESA data\\working data\\wide format files\\nesa_entities_wide' + date + '.csv', encoding = "ISO-8859-1")


columns = nesa_df_wide.columns.tolist()

columns_new = []

for item in columns:
	item_new  = str(nesa_df_wide[item].iloc[0]) + '_' + item.split('.')[0] + '_'  + str(nesa_df_wide[item].iloc[1]) + '_' + str(nesa_df_wide[item].iloc[2])
	item_new = item_new.lower()
	columns_new.append(item_new)


nesa_df_wide.columns = columns_new
nesa_df_wide.rename(columns = {'subject_grade_demographic_type_demographic':'entity_id', 'nan_unnamed: 1_nan_nan': 'school_year'}, inplace = True)

nesa_df_wide = nesa_df_wide.ix[4:]

nesa_df_wide.to_csv('C:\\Users\\KLA\\Dropbox\\MHC OPS Absent Narratives Approach\\Evaluation (All) 2016-2017\\Data\\NESA data\\working data\\nesa_entities_wide_formatted_' + date + '.csv')

'''