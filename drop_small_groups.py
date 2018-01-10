import pandas as pd
print(pd.__version__)
import datetime as dt
import numpy as np     
date = dt.datetime.today().strftime("%m%d%Y")


data_path = 'C:\\Users\\KLA\\Dropbox\\MHC OPS Absent Narratives Approach\\Evaluation (All) 2016-2017\\Data\\School master data\\frozen data\\schools_all_wide_02152017.csv'
data = pd.read_csv(data_path, encoding  = "ISO-8859-1")

##this creates a dataframe of the columns to look at and see if less than 10
to_examine_df = data.ix[:,'amer_indian2011-2012':'white2015-2016']

##this turns the columns in that data frame into a list
to_examine = list(to_examine_df.columns)

print(to_examine)
##this works


	
#this creates a data frame and then list of columns for those in the nesa data we need to drop cells from if too small of group
to_drop_if_df = data.ix[:, 'math_3_ell_n2011-2012':'writ_11_spec_ed_y2015-2016']
to_drop_if = list(to_drop_if_df.columns)


to_drop_if_df = pd.DataFrame(to_drop_if)

to_drop_if_df.columns = ['variables']

expanded = to_drop_if_df['variables'].str.split('_', expand=True)

#expanded[3] = expanded[3].replace(regex=True,to_replace=r'[a-zA-Z]+',value=r'')

to_drop_if_df = pd.concat([to_drop_if_df,expanded], axis=1)



del to_drop_if_df[0]
del to_drop_if_df[1]


'''
don't run this part because we actually want to get rid of these too

to_drop_if_df = to_drop_if_df[~to_drop_if_df['variables'].str.contains('ell_n')]
to_drop_if_df = to_drop_if_df[~to_drop_if_df['variables'].str.contains('frl_sp')]
to_drop_if_df = to_drop_if_df[~to_drop_if_df['variables'].str.contains('spec_ed_n')]

'''


to_drop_if_df['school_year'] = to_drop_if_df['variables'].str[-9:]

# Set a default value
to_drop_if_df['name'] = None

race = to_drop_if_df[to_drop_if_df[2] == 'race']

not_race = to_drop_if_df[to_drop_if_df[2] != 'race']

print(race.head())


race['name'] = race[3] + '_' + race[4]

race['name'] = race['name'].fillna(race[3])

del race[3]
del race[4]

race.to_csv('C:\\Users\\KLA\\Dropbox\\MHC OPS Absent Narratives Approach\\Evaluation (All) 2016-2017\\Data\\School master data\\working data\\test_race_drop_small.csv')

not_race[2] = not_race[2].replace(to_replace = 'spec', value = 'spec_ed')

not_race['name'] = not_race[2] + not_race['school_year']

del not_race[3]
del not_race[4]


to_drop = pd.concat([race, not_race])

'''

# Set Age_Group value for all row indexes which Age are greater than 40
df['Age_Group'][df['Age'] > 40] = '>40'
# Set Age_Group value for all row indexes which Age are greater than 18 and < 40
df['Age_Group'][(df['Age'] > 18) & (df['Age'] < 40)] = '>18'
# Set Age_Group value for all row indexes which Age are less than 18
df['Age_Group'][df['Age'] < 18] = '<18'


if to_drop_if_df[2] == 'race':
	to_drop_if_df['name'] = to_drop_if_df[3] + '_' + to_drop_if_df[4]
else:
	to_drop_if_df['name'] = NaN


to_drop_if_df[2].lambda x: x.drop_small

'''

to_drop.to_csv('C:\\Users\\KLA\\Dropbox\\MHC OPS Absent Narratives Approach\\Evaluation (All) 2016-2017\\Data\\School master data\\working data\\test_drop_small_three.csv')


