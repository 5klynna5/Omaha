##cd C:\\Users\KLA\Dropbox\MHC OPS Absent Narratives Approach\Evaluation (All) 2015-2016\Evaluation Methods\Surveys\Story Circle Cohort

###import dependencies
import pandas as pd
import numpy as np
#import matplotlib.pyplot as plt
import ntpath
from collections import Counter

###read in survey export file

results_path = 'C:\\Users\KLA\Dropbox\\MHC OPS Absent Narratives Approach\Evaluation (all) 2017-2018\\2017-2018 Evaluation Methods\Surveys\\fa17 Post Offering Surveys\\survey results RC fa17\\fa17_rcwse_survey_results.csv'
results = pd.read_csv(results_path, encoding = "utf-8")

###create object for file name

results_name = ntpath.basename(results_path).rstrip('_results.csv')
results_directory = ntpath.dirname(results_path)

###drop off extra header row
results = results.drop(1)
results = results.drop(0)

###drop off useless columns
results = results.drop(results.columns[0:7], axis=1)
results = results.drop(results.columns[6:10], axis=1)

### read in codebook

codebook = pd.read_csv('C:\\Users\\KLA\\Dropbox\\MHC OPS Absent Narratives Approach\\Evaluation (all) 2017-2018\\2017-2018 Evaluation Methods\\Surveys\\survey_codebook_fa17.csv', encoding = "ISO-8859-1")

###put updated list of column labels as columns of dataframe
columns = codebook['new_labels'].tolist()

###for just story circle cohort, this question doesn't exist, remove
#columns.remove('strategy_other')

results.columns = columns

print(results.head())

###entity field, remove ops from end
##only do this for those surveys where entity is included in survey

results['entity'] = results['entity'].map(lambda x: x.rstrip(' - OPS'))

###create first and last name fields - not necessary 17-18 because first and last exist in data
##results['first_name'] = results['name'].apply(lambda x: pd.Series(x.split(',')))[1]
##results['last_name'] = results['name'].apply(lambda x: pd.Series(x.split(',')))[0]

##for sms
##results['first_name'] = results['name']
##results['last_name'] = results['name']

###create full name field combining first and last name

results['full_name'] = results['first_name'] + ' ' + results['last_name']

##create column that pulls self-reported entity, when that data is missing, 
#pull the mhc reported entity from registration data

#for rc use these 2 lines and comment out next line
#results['offering'] = results['entity']
#del results['entity']

results['entity_merged'] = results['entity_self_report'].fillna(results['entity'])

##create semester and offering fields from the file name
#have to add + 's' to results_name_simple for sms, + se for rcwse. Why is this??

results_name_simple = results_name[:-7] 
results['semester']= results_name_simple.split('_', 1)[0]
#comment out next line for rc
results['offering']= results_name_simple.split('_', 1)[1]


###create column with number of missing values in row
results['number_nan'] = results.isnull().sum(axis=1)

##drop rows if they are all missing data, this number should be 80 for most offerings, 78 for fa15 scc
results = results[results.number_nan < 80]

###save cleaned version of data as csv

results.to_csv(results_directory + '\\' + results_name + '_cleaned.csv')

###save to folder for jeff
results.to_csv('C:\\Users\\KLA\\Dropbox\\MHC OPS Absent Narratives Approach\\Evaluation (All) 2017-2018\\2017-2018 Evaluation Methods\\Surveys\\cleaned_survey_results\\' + results_name + '_cleaned.csv')


###here begins analysis for individual survey reports
###checking total n by looking at how many rows in data

total_n = len(results)

###here begins analysis of student level impacts
###create list of student level impacts

student_level_impacts = ['I give students more individual attention',
'I more frequently encourage students to think critically about what they are learning',
'I am more frequently including student\'s own perspectives within my curriculum',
'I feel less confident in my ability to teach my students',
'My students seem to have an increased sense of belonging in the classroom',
'I send students out of the classroom for behavior issues less frequently',
'I feel more distant from some of my students',
'I have stronger relationships with some of my students']

###creating list of counting if each student level impact is happening because of this offering

because_off_students = [results['off_student_attn'].str.contains('Because').sum(),
results['off_critical_think'].str.contains('Because').sum(),
results['off_student_persp'].str.contains('Because').sum(),
results['off_less_conf'].str.contains('Because').sum(),
results['off_student_belong'].str.contains('Because').sum(),
results['off_less_sendout'].str.contains('Because').sum(),
results['off_distant_students'].str.contains('Because').sum(),
results['off_stronger_relationships'].str.contains('Because').sum()]


###creating data frame of name of student level impact, number experiencing because of offering, and total n
student_impacts = pd.DataFrame({'student level impacts': student_level_impacts, 'number because of offering' : because_off_students})
student_impacts['total_n'] = total_n

#rearranging columns to match template in excel for creating chart

student_impacts = student_impacts[['total_n','number because of offering', 'student level impacts']]

###writing to csv (can we make this name it based on what file is written in so we can see what survey?)

student_impacts.to_csv(results_directory + '\\' + results_name + '_student_impacts.csv')



##### here starts student engagement and academic growth analysis

student_engage = [results['engagement'].str.contains('MOST').sum(), 
results['engagement'].str.contains('SOME').sum(), 
results['engagement'].str.contains('think').sum()]


student_acad = [results['academic_growth'].str.contains('MOST').sum(),
results['academic_growth'].str.contains('SOME').sum(),
results['academic_growth'].str.contains('think').sum()]

most_some_no_list = ['MOST', 'SOME', 'NO_IMPACT']


engage_acad = pd.DataFrame({'level' : most_some_no_list, 'Student Academic Growth' : student_acad, 'Student Engagement' : student_engage})

engage_acad.to_csv(results_directory + '\\' + results_name + '_engage_acad.csv')


#### here starts educator etc. impact

###creating list of all educ, school, etc. level impacts

educ_level_impacts = ['I feel more distant from most of my colleagues',
'I am part of a group of educators (community of practice) within my school that works together on concepts from Minnesota Humanities Center offerings', 
'I am more often confronting other educators on practices that might be damaging to a student', 
'I feel like I know less than I did before taking this offering',
'I am part of positive change happening within my school community',
'I am part of a group of educators (community of practice) with people from other schools in the district that works together on concepts we learned in Minnesota Humanities Center offerings',
'I am using different language to talk about students',
'I am more frequently in two-way dialogue with students\' parents']


###counting if each impact is happening because of this offering and creating as list

because_off_educ = [results['off_distant_colleag'].str.contains('Because').sum(),
results['off_commun_school'].str.contains('Because').sum(),
results['off_confront_educs'].str.contains('Because').sum(),
results['off_know_less'].str.contains('Because').sum(),
results['off_pos_change'].str.contains('Because').sum(),
results['off_commun_district'].str.contains('Because').sum(),
results['off_diff_lang'].str.contains('Because').sum(),
results['off_parent_dialog'].str.contains('Because').sum(),]

###creating data frame of name of educ level impact, number experiencing because of offering, and total n

educ_impacts = pd.DataFrame({'educ level impacts': educ_level_impacts, 'number because of offering' : because_off_educ})
educ_impacts['total_n'] = total_n

###putting columns in order I want

educ_impacts = educ_impacts[['total_n','number because of offering', 'educ level impacts']]

###export to csv

educ_impacts.to_csv(results_directory + '\\' + results_name + '_educ_impacts.csv')

###here starts empathy table

###create list of empathy impacts
empathy_impacts = ['I  picture myself in the place of my students when I hear about their lives outside of the classroom',
'When I hear about the lives of my students outside of the classroom, I  want to know more',
'Hearing about my students\' life experiences affects me emotionally',
'When hearing about a student\'s life outside of the classroom, I have a vivid image of what it is like',
'I feel overwhelmed when I think about my students\' lives']


empathy_list = ['emp_pic_myself', 'emp_know_more', 'emp_emotion', 'emp_image', 'emp_overwhelmed']


empathy = pd.DataFrame(columns=['mean_before', 'mean_now', 'n_before', 'n_now'])

###remove row if item + '_before' value or item + '_now' value is not_null

for item in empathy_list:
	emp_df = results.dropna(how = 'any', subset = [item +'_before', item + '_now'])
	item = ([emp_df[item +'_before'].astype(float).mean(), emp_df[item + '_now'].astype(float).mean(), emp_df[item + '_before'].count(), emp_df[item + '_now'].count()])
	empathy = empathy.append(pd.Series(item, index = ['mean_before', 'mean_now', 'n_before', 'n_now']), ignore_index=True)

empathy['impacts'] = empathy_impacts

print(empathy)

###export to csv

empathy.to_csv(results_directory + '\\' + results_name + '_empathy.csv')



###daily outlook analysis
### maybe could do this more simply with value counts and series to dataframe?

outlook_vals = [results['outlook'].str.contains('less').sum(), 
results['outlook'].str.contains('impacted').sum(), 
results['outlook'].str.contains('more').sum()]

outlook_list = ['less', 'no_impact', 'more']

outlook_tab = pd.DataFrame({'response' : outlook_list, 'vals' : outlook_vals})

outlook_tab.to_csv(results_directory + '\\' + results_name + '_outlook.csv')


####strategies for first time

strategies_first_time = results[['strategy', 'first_time']]
strategies_first = strategies_first_time.pivot_table(index='strategy', columns='first_time', aggfunc = len, fill_value = 0)

#list_strategies = pd.unique(results['strategy'].ravel())

strategies_tried = Counter(results['strategy'])

strat = pd.Series(strategies_tried, name='number')
strat.index.name = 'strategy'
strat.reset_index()

strategy_tried = pd.Series.to_frame(strat)

strategies_all = strategies_first.join(strategy_tried)

strategies_all.to_csv(results_directory + '\\' + results_name + '_strategies_first_time.csv')

###impacts for all strategies

myself = results['myself'].value_counts()
my_students = results['my_students'].value_counts()
other_students = results['other_students'].value_counts()
classroom = results['classroom'].value_counts()
colleagues = results['colleagues'].value_counts()
school = results['school'].value_counts()
district = results['district'].value_counts()

impacts_strategies = myself.append(my_students)
impacts_strategies = impacts_strategies.append(other_students)
impacts_strategies = impacts_strategies.append(classroom)
impacts_strategies = impacts_strategies.append(colleagues)
impacts_strategies = impacts_strategies.append(school)
impacts_strategies = impacts_strategies.append(district)

impacts_n = strategy_tried['number'].sum()

impacts_strategies = pd.DataFrame({'impacts' : pd.Series(impacts_strategies) , 'impacts_n' : impacts_n})

impacts_strategies.to_csv(results_directory + '\\' + results_name + '_impacts_all_strategies.csv')

###comfort sharing
safety_values = results['safe_sharing'].value_counts()
safety_tab = pd.Series.to_frame(safety_values)

safety_tab = safety_tab.reindex(["Never", "Sometimes", "Most of the time", "Always"])

safety_tab.to_csv(results_directory + '\\' + results_name + '_safe_sharing.csv')

###impacts for each strategy
