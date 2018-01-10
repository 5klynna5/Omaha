import pandas as pd
print(pd.__version__)
import datetime as dt
import numpy as np     
date = dt.datetime.today().strftime("%m%d%Y")
import os
import glob

directory_16_17 = 'C:\\Users\\KLA\\Dropbox\\MHC OPS Absent Narratives Approach\\Evaluation (All) 2016-2017\\Evaluation Methods\Surveys\\cleaned_survey_results'

allFiles = glob.glob(directory_16_17 + "/*.csv")
all_surveys = pd.DataFrame()
list_ = []
for file_ in allFiles:
    df = pd.read_csv(file_, encoding = "ISO-8859-1")
    list_.append(df)

all_surveys = pd.concat(list_)

del all_surveys['Unnamed: 0']

print(all_surveys.columns)

all_surveys.to_csv('C:\\Users\\KLA\\Dropbox\\MHC OPS Absent Narratives Approach\\Evaluation (All) 2016-2017\\Evaluation Methods\\Surveys\\16_17_cohort_survey_results.csv')
