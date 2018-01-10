import pandas as pd
print(pd.__version__)
import datetime as dt     
date = dt.datetime.today().strftime("%m%d%Y")

tabl_orig_path = 'C:\\Users\KLA\Dropbox\MHC OPS Absent Narratives Approach\Evaluation (All) 2016-2017\Data\\Tableau Data File_two.csv'
tabl_orig_df = pd.read_csv(tabl_orig_path, encoding = "ISO-8859-1" )

new_path = 'C:\\Users\KLA\Dropbox\MHC OPS Absent Narratives Approach\Evaluation (All) 2016-2017\Data\\attended_events_for_tableau_11142016.csv'
new_df = pd.read_csv(new_path, encoding = "ISO-8859-1" )

diff_columns = [obj for obj in tabl_orig_df.columns if obj not in new_df.columns]
print(diff_columns)

del new_df['Unnamed: 0']
del new_df['number']


new_df['lastfirstname'] = new_df['full_name'].str.split(' ').str[1] + ', ' + new_df['full_name'].str.split(' ').str[0]

new_df['simplesemester'] = new_df['semester'].str.split(' ').str[0]

new_df['entry_id'] = new_df['person_id'].astype(str) + new_df['program_id'].astype(str)

print(new_df.head())

new_df.to_csv('C:\\Users\KLA\Dropbox\MHC OPS Absent Narratives Approach\Evaluation (All) 2016-2017\Data\\Tableau School Profiles\\tableau_compiled_11142016.csv')