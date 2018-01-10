import pandas as pd
print(pd.__version__)
import datetime as dt
import numpy as np     
date = dt.datetime.today().strftime("%m%d%Y")
import os
import glob

fa16_path = 'C:\\Users\\KLA\\Dropbox\\MHC OPS Absent Narratives Approach\\Evaluation (All) 2016-2017\\Evaluation Methods\\Surveys\\Fall 2016 Combined Results\\all_fa16_survey_results.csv'

fa_16 = pd.read_csv(fa16_path, encoding = "ISO-8859-1")

directory_15_16 = 'C:\\Users\\KLA\\Dropbox\\MHC OPS Absent Narratives Approach\\Evaluation (All) 2015-2016\\Evaluation Methods\Surveys\\2015-2016 cohort survey results'

allFiles = glob.glob(directory_15_16 + "/*.csv")
all_15_16 = pd.DataFrame()
list_ = []
for file_ in allFiles:
    df = pd.read_csv(file_, encoding = "ISO-8859-1")
    list_.append(df)
list_.append(fa_16)
all_surveys = pd.concat(list_)

del all_surveys['Unnamed: 0']

print(all_surveys.columns)

all_surveys.to_csv('C:\\Users\\KLA\\Dropbox\\MHC OPS Absent Narratives Approach\\Evaluation (All) 2016-2017\\Evaluation Methods\\Surveys\\fa15_to_fa16_cohort_survey_results.csv')
