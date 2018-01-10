import pandas as pd
import difflib 
import numpy as np


path_partic = 'C:\\Users\KLA\Dropbox\MHC OPS Absent Narratives Approach\Evaluation (All) 2015-2016\Data\Participation Files from MHC\working data\KA working files\\mhc-ops_participation_all_to_20160512_KA.csv'
partic_df = pd.read_csv(path_partic)

path_impact_climate = 'C:\\Users\KLA\Dropbox\MHC OPS Absent Narratives Approach\Evaluation (All) 2015-2016\Data\OPS Data\Working Data\Climate Survey Data\Processed data\\processed_Q34_ELL.csv'
impact_df = pd.read_csv(path_impact_climate)

path_entity_ids = 'C:\\Users\KLA\Dropbox\MHC OPS Absent Narratives Approach\Evaluation (All) 2015-2016\Data\Participation Files from MHC\working data\KA working files\\entity_codebook.csv'
entity_df = pd.read_csv(path_entity_ids)

entity_ops = entity_df[(entity_df['entity_parent'] == 'OPS')]

impact_df['entity'] = impact_df['entity'].str.upper()

impact_df['entity_first'] = impact_df['entity'].str.split(' ').str[0]
entity_ops['entity_first'] = entity_ops['entity'].str.split(' ').str[0]

print(impact_df['entity_first'].head())
print(entity_ops['entity_first'].head())


def match(string_a,string_b):
  if string_a.str.contains(string_b):
    return string_a
  else:
    return np.NaN



'''

def fuzzy_match(x, list_strings):

  best_match = None
  highest_jw = 0

  for current_string in list_strings:
    current_score = jellyfish.jaro_winkler(x, current_string)

    if(current_score > highest_jw):
      highest_jw = current_score
      best_match = current_string

  return best_match

def fuzzy_match(a, b):
    left = '1' if pd.isnull(a) else a
    right = b.fillna('2')
    out = difflib.get_close_matches(left, right, n=1, cutoff=0.9)
    return out[0] if out else np.NaN

'''

impact_df['entity_clean'] = impact_df['entity'].map(lambda x: match(x, entity_ops['entity']))


impact_entity_df = pd.merge(impact_df, entity_ops, on='entity', how='right')

impact_entity_df.to_csv('.\esl_impact_cleaned_entity_091316.csv')

##df1.join(df2)