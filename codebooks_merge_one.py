import pandas as pd
print(pd.__version__)
import datetime as dt     
date = dt.datetime.today().strftime("%m%d%Y")

jeff_codebook_path = 'C:\\Users\\KLA\\Dropbox\\MHC OPS Absent Narratives Approach\\Evaluation (All) 2015-2016\\Data\\Participation Files from MHC\\working data\\KA working files\\entity_codebook.csv'

jeff_cb = pd.read_csv(jeff_codebook_path, encoding = "ISO-8859-1")

kirsten_codebook_path = 'C:\\Users\\KLA\\Dropbox\\MHC OPS Absent Narratives Approach\\Evaluation (All) 2016-2017\\Data\\School master data\\working data\\fall_data_entity_codebook.csv'

kirsten_cb = pd.read_csv(kirsten_codebook_path, encoding = "ISO-8859-1")
 

cb = pd.merge(jeff_cb, kirsten_cb, how = "outer", on = "entity_id")

cb.to_csv('C:\\Users\\KLA\\Dropbox\\MHC OPS Absent Narratives Approach\\Evaluation (All) 2015-2016\\Data\\Participation Files from MHC\\working data\\KA working files\\entity_codebook_fa16.csv')

del cb['entity_y']
del cb['school']

cb['entity'] = cb['entity_x']

del cb['entity_x']

print(cb.head())
