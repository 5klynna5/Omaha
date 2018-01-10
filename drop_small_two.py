import pandas as pd
print(pd.__version__)
import datetime as dt
import numpy as np     
date = dt.datetime.today().strftime("%m%d%Y")

data_path = 'C:\\Users\\KLA\\Dropbox\\MHC OPS Absent Narratives Approach\\Evaluation (All) 2016-2017\\Data\\School master data\\frozen data\\schools_all_wide_02152017.csv'
data = pd.read_csv(data_path, encoding  = "ISO-8859-1")

to_drop = pd.read_csv('C:\\Users\\KLA\\Dropbox\\MHC OPS Absent Narratives Approach\\Evaluation (All) 2016-2017\\Data\\School master data\\working data\\test_drop_small_three.csv', encoding = "ISO-8859-1")


drop = to_drop[['variables', 'name']]


##this works for individual column
#data['math_3_race_amer_indian2011-2012'] = np.where(data['amer_indian2011-2012'] < 10, None, data['math_3_race_amer_indian2011-2012'])

for row in drop:
	data[drop['variables']] = np.where(data[drop['name']] < 10, None, data[drop['variables']])

del data['Unnamed: 0']


data.to_csv('C:\\Users\\KLA\\Dropbox\\MHC OPS Absent Narratives Approach\\Evaluation (All) 2016-2017\\Data\\School master data\\working data\\test_drop_all.csv')

print(data[['spec_ed2013-2014','math_5_spec_ed_y2013-2014']])