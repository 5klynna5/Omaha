data <- read.csv(file.choose())

names(data)

columns_all_yrs <- c("total_enroll_avr11.12to14.15", 
                     "suspend_percent_change_12_13_to_14_15",
                     "percent_suspend_stud_avr11.12to14.15", 
                     "percent_spec_ed_stud_avr11.12to14.15",
                     "percent_minority_stud_avr11.12to14.15",
                     "percent_frl_stud_avr11.12to14.15",
                     "percent_ell_stud_avr11.12to14.15",
                     "percent_cum_offering2014.2015",
                     "percent_cum_num_offering_participants2014.2015",
                     "percent_cum_num_more_than_one_core_offering_participants2014.2015",
                     "partner_num2014.2015",
                     "participation_cat_binary_sum11.12to14.15",
                     #"participation_cat_11.12to14.15",
                     "num_cum_school_based_events2014.2015",
                     "mobility_percent_avr11.12to14.15")

cor(data[columns_all_yrs], method = "pearson", use = "pairwise.complete.obs")
