library(ggplot2)
library(psych)

data <- read.csv(file.choose())

names(data)
data$participation_binary <- with(data,ifelse(participation_cat_binary_sum11.12to14.15 == "0", 0, 1))

columns_total_analysis <- c('percent_ell_stud_avr11.12to14.15',
                            'attend_percent_avr11.12to14.15',
                            'total_enroll_avr11.12to14.15',
                            #'entity_type',
                            'mobility_percent_avr11.12to14.15',
                            'percent_frl_stud_avr11.12to14.15',
                            'percent_minority_stud_avr11.12to14.15',
                            'percent_suspend_stud_avr11.12to14.15',
                            'percent_cum_core_offering2014.2015',
                            'partner_num2014.2015',
                            #'participation_cat_11.12to14.15',
                            #'participation_cat_binary_sum11.12to14.15',
                            'percent_cum_num_offering_participants2014.2015',
                            'percent_cum_offering2014.2015',
                            'percent_cum_num_more_than_one_core_offering_participants2014.2015',
                            'num_cum_school_based_events2014.2015',
                            'hispanic_gap_change_total',
                            'black_gap_change_total',
                            'pac_islander_gap_change_total',
                            'amer_indian_gap_change_total',
                            'asian_gap_change_total',
                            'total_minority2014.2015')


cor(data[columns_total_analysis], method = 'pearson')

qqnorm(data$hispanic_gap_change_total,main="Normal Q-Q Plot partners")
hist(data$hispanic_gap_change_total)
plot(density(na.omit(data$hispanic_gap_change_total)))

qqnorm(data$black_gap_change_total,main="Normal Q-Q Plot partners")
hist(data$black_gap_change_total)
plot(density(na.omit(data$black_gap_change_total)))

###cannot use this, only 5 points
qqnorm(data$pac_islander_gap_change_total,main="Normal Q-Q Plot partners")
hist(data$pac_islander_gap_change_total)
plot(density(na.omit(data$pac_islander_gap_change_total)))
###########

###pretty perfectly normal###
qqnorm(data$asian_gap_change_total,main="Normal Q-Q Plot partners")
hist(data$asian_gap_change_total)
plot(density(na.omit(data$asian_gap_change_total)))
############

####pretty perfectly normal###
qqnorm(data$amer_indian_gap_change_total,main="Normal Q-Q Plot partners")
hist(data$amer_indian_gap_change_total)
plot(density(na.omit(data$amer_indian_gap_change_total)))
###########

###I will move forward looking at black, hispanic, asian, and amer_indian gap change totals

lm_everything_black <- lm(black_gap_change_total ~ percent_black_stud2013.2014
                          + total_enroll_avr11.12to14.15 + mobility_percent_avr11.12to14.15 +
                            percent_frl_stud_avr11.12to14.15 + percent_minority_stud_avr11.12to14.15 + percent_suspend_stud_avr11.12to14.15
                          + percent_cum_core_offering2013.2014 + partner_num2013.2014 + participation_cat_11.12to14.15 + participation_cat_binary_sum11.12to14.15
                          + percent_cum_num_offering_participants2013.2014 + percent_cum_offering2013.2014
                          + percent_cum_num_more_than_one_core_offering_participants2013.2014 + num_cum_school_based_events2013.2014 + black_gap2011.2012, data = data)
summary(lm_everything_black)

lm_model_black <- lm(black_gap_change_total ~ percent_cum_num_more_than_one_core_offering_participants2014.2015 + black_gap2011.2012, data = data)
summary(lm_model_black)
coef(lm_model_black)

lm_model_black_two <- lm(black_gap_change_total ~
                          + total_enroll_avr11.12to14.15 + percent_minority_stud_avr11.12to14.15 + percent_suspend_stud_avr11.12to14.15
                          + black_gap2011.2012, data = data)
summary(lm_model_black_two)
plot(lm_model_black_two)

lm_everything_black_read <- lm(black_gap_change_total ~ percent_black_stud2013.2014
                          + total_enroll_avr11.12to14.15 + mobility_percent_avr11.12to14.15 +
                            percent_frl_stud_avr11.12to14.15 + percent_minority_stud_avr11.12to14.15 + percent_suspend_stud_avr11.12to14.15
                          + percent_cum_core_offering2013.2014 + partner_num2013.2014 + participation_cat_binary_sum11.12to14.15
                          + percent_cum_num_offering_participants2013.2014 + percent_cum_offering2013.2014
                          + percent_cum_num_more_than_one_core_offering_participants2013.2014 + num_cum_school_based_events2013.2014 + black_gap2011.2012, data = data)
summary(lm_everything_black_read)

lm_black_read <- lm(black_gap_change_total ~ percent_black_stud2013.2014
                               + percent_suspend_stud_avr11.12to14.15
                               + participation_cat_binary_sum11.12to14.15 + black_gap2011.2012, data = data)
summary(lm_black_read)

plot(data$black_gap_change_total, data$black_gap2011.2012)


plot(PeerRat ~ GRE, data = educ, 
     xlab = "Average GRE Score", 
     ylab = "Peer Rating", 
     bty = "l"
)
abline(a = 4.75, b = 63.32, col = "green")
abline(a = -10.59, b = 63.32, col = "blue")
abline(a = -25.93, b = 63.32, col = "red")
legend("topleft", 
       legend = c("Large Programs", "Medium Programs", "Small Programs"), 
       lty = c(1, 1, 1), 
       col = c("green", "blue", "red"), 
       inset = 0.02
)



plot(data$black_gap_change_total, data$percent_cum_num_more_than_one_core_offering_participants2014.2015)
abline(lm_model_black)
plot(lm_model_black)


abline(h = 0)
abline(h = c(-2, 2), lty = "dotted")

lm_everything_hispanic <- lm(hispanic_gap_change_total ~ percent_hispanic_stud2014.2015 + attend_percent_avr11.12to14.15
                          + total_enroll_avr11.12to14.15 + entity_type + mobility_percent_avr11.12to14.15 +
                            percent_frl_stud_avr11.12to14.15 + percent_minority_stud_avr11.12to14.15 + percent_suspend_stud_avr11.12to14.15
                          + percent_cum_core_offering2014.2015 + partner_num2014.2015 + participation_cat_11.12to14.15 + participation_cat_binary_sum11.12to14.15
                          + participation_binary + percent_cum_num_offering_participants2014.2015 + percent_cum_offering2014.2015
                          + percent_cum_num_more_than_one_core_offering_participants2014.2015 + num_cum_school_based_events2014.2015 + hispanic_gap2011.2012, data = data)
summary(lm_everything_hispanic)

lm_model_hispanic <- lm(hispanic_gap_change_total ~
                             total_enroll_avr11.12to14.15
                           + percent_minority_stud_avr11.12to14.15
                             + hispanic_gap2011.2012, data = data)
summary(lm_model_hispanic)


lm_everything_hispanic_read <- lm(hispanic_gap_change_total ~ percent_hispanic_stud2014.2015 + attend_percent_avr11.12to14.15
                             + total_enroll_avr11.12to14.15 + mobility_percent_avr11.12to14.15 +
                               percent_frl_stud_avr11.12to14.15 + percent_minority_stud_avr11.12to14.15 + percent_suspend_stud_avr11.12to14.15
                             + percent_cum_core_offering2014.2015 + partner_num2014.2015 + participation_cat_binary_sum11.12to14.15
                             + participation_binary + percent_cum_num_offering_participants2014.2015 + percent_cum_offering2014.2015
                             + percent_cum_num_more_than_one_core_offering_participants2014.2015 + num_cum_school_based_events2014.2015 + hispanic_gap2011.2012, data = data)
summary(lm_everything_hispanic_read)

lm_hispanic_read <- lm(hispanic_gap_change_total ~ percent_hispanic_stud2014.2015
                                 + percent_minority_stud_avr11.12to14.15 + percent_suspend_stud_avr11.12to14.15
                                  + hispanic_gap2011.2012, data = data)
summary(lm_hispanic_read)

lm_everything_amer_indian_read <- lm(amer_indian_gap_change_total ~ percent_amer_indian_stud2014.2015 + attend_percent_avr11.12to14.15
                               + total_enroll_avr11.12to14.15 + mobility_percent_avr11.12to14.15 +
                                 percent_frl_stud_avr11.12to14.15 + percent_minority_stud_avr11.12to14.15 + percent_suspend_stud_avr11.12to14.15
                               + percent_cum_core_offering2014.2015 + partner_num2014.2015 + participation_cat_binary_sum11.12to14.15
                               + participation_binary + percent_cum_num_offering_participants2014.2015 + percent_cum_offering2014.2015
                               + percent_cum_num_more_than_one_core_offering_participants2014.2015 + num_cum_school_based_events2014.2015 + amer_indian_gap2011.2012, data = data)
summary(lm_everything_amer_indian_read)

lm_amer_indian_read <- lm(amer_indian_gap_change_total ~ percent_cum_num_more_than_one_core_offering_participants2014.2015 + amer_indian_gap2011.2012, data = data)
summary(lm_amer_indian_read)

lm_model_amer_indian <- lm(amer_indian_gap_change_total ~ 
                            amer_indian_gap2011.2012, data = data)
summary(lm_model_amer_indian)

lm_everything_asian_read <- lm(asian_gap_change_total ~ percent_asian_stud2014.2015 + attend_percent_avr11.12to14.15
                                  + total_enroll_avr11.12to14.15 + mobility_percent_avr11.12to14.15 +
                                    percent_frl_stud_avr11.12to14.15 + percent_minority_stud_avr11.12to14.15 + percent_suspend_stud_avr11.12to14.15
                                  + percent_cum_core_offering2014.2015 + partner_num2014.2015 + participation_cat_binary_sum11.12to14.15
                                  + participation_binary + percent_cum_num_offering_participants2014.2015 + percent_cum_offering2014.2015
                                  + percent_cum_num_more_than_one_core_offering_participants2014.2015 + num_cum_school_based_events2014.2015 + asian_gap2011.2012, data = data)
summary(lm_everything_asian_read)

lm_asian_read <- lm(asian_gap_change_total ~ percent_asian_stud2014.2015
                               + percent_suspend_stud_avr11.12to14.15
                               + percent_cum_num_more_than_one_core_offering_participants2014.2015 + asian_gap2011.2012, data = data)
summary(lm_asian_read)

lm_asian <- lm(asian_gap_change_total ~ num_cum_school_based_events2014.2015
                             + percent_suspend_stud_avr11.12to14.15
                             + asian_gap2011.2012, data = data)
summary(lm_asian)

plot(data$asian_gap_change_total, data$num_cum_school_based_events2014.2015)
ggplot(data = data, aes(x = asian_gap_change_total, y = num_cum_school_based_events2014.2015)) +
  geom_point() +
  geom_smooth(method = "lm")

columns_2014.2015_analysis <- c('percent_more_than_one_core_offering2014.2015',
                                'percent_offering2014.2015',
                                #'partner_status2014.2015',
                                'partner_num2014.2015',
                                #'participation_cat2014.2015',
                                #'participation_cat_binary2014.2015',
                                'percent_cum_num_offering_participants2014.2015',
                                'percent_cum_offering2014.2015',
                                'percent_cum_num_more_than_one_core_offering_participants2014.2015',
                                'percent_core_offering2014.2015',
                                'num_school_based_events2014.2015',
                                'total_enroll2014.2015',
                                'percent_minority_stud2014.2015',
                                'percent_hispanic_stud2014.2015',
                                'percent_ell_stud2014.2015',
                                'num_cum_school_based_events2014.2015',
                                'hispanic_gap_change2014.2015',
                                'hispanic_gap2013.2014')

cor(data[columns_2014.2015_analysis], method = 'pearson', use ='pairwise.complete.obs')

lm_everything_hisp_2014.2015 <- lm(hispanic_gap_change2014.2015 ~ percent_more_than_one_core_offering2014.2015 +
  percent_offering2014.2015 + partner_status2014.2015 + partner_num2014.2015 + participation_cat2014.2015 + participation_cat_binary2014.2015 
+ percent_cum_num_offering_participants2014.2015 + percent_cum_offering2014.2015 + percent_cum_num_more_than_one_core_offering_participants2014.2015
+ percent_core_offering2014.2015 + num_school_based_events2014.2015 + total_enroll2014.2015 + percent_minority_stud2014.2015
+ percent_hispanic_stud2014.2015 + percent_ell_stud2014.2015 + num_cum_school_based_events2014.2015 + hispanic_gap2013.2014, data = data)

summary(lm_everything_hisp_2014.2015)

lm_hisp_2014.2015 <- lm(hispanic_gap_change2014.2015 ~ 
                                     participation_cat2014.2015 
                                  + percent_minority_stud2014.2015
                                   + hispanic_gap2013.2014, data = data)

summary(lm_hisp_2014.2015)

plot(data$percent_minority_stud2014.2015, data$hispanic_gap_change2014.2015)

lm_everything_hisp_2013.2014 <- lm(hispanic_gap_change2013.2014 ~ percent_more_than_one_core_offering2013.2014 +
                                     percent_offering2013.2014 + partner_status2013.2014 + partner_num2013.2014 + participation_cat2013.2014 + participation_cat_binary2013.2014 
                                   + percent_cum_num_offering_participants2013.2014 + percent_cum_offering2013.2014 + percent_cum_num_more_than_one_core_offering_participants2013.2014
                                   + percent_core_offering2013.2014 + num_school_based_events2013.2014 + total_enroll2013.2014 + percent_minority_stud2013.2014
                                   + percent_hispanic_stud2013.2014 + percent_ell_stud2013.2014 + num_cum_school_based_events2013.2014 + hispanic_gap2012.2013, data = data)

summary(lm_everything_hisp_2013.2014)

lm_hisp_2013.2014 <- lm(hispanic_gap_change2013.2014 ~ 
                                     total_enroll2013.2014 + percent_minority_stud2013.2014
                                   + hispanic_gap2012.2013, data = data)

summary(lm_hisp_2013.2014)

lm_everything_hisp_2012.2013 <- lm(hispanic_gap_change2012.2013 ~ percent_more_than_one_core_offering2012.2013 +
                                     percent_offering2012.2013 + partner_status2012.2013 + partner_num2012.2013 + participation_cat2012.2013 + participation_cat_binary2012.2013 
                                   + percent_cum_num_offering_participants2012.2013 + percent_cum_offering2012.2013 + percent_cum_num_more_than_one_core_offering_participants2012.2013
                                   + percent_core_offering2012.2013 + num_school_based_events2012.2013 + total_enroll2012.2013 + percent_minority_stud2012.2013
                                   + percent_hispanic_stud2012.2013 + percent_ell_stud2012.2013 + num_cum_school_based_events2012.2013 + hispanic_gap2011.2012, data = data)

summary(lm_everything_hisp_2012.2013)

lm_hisp_2012.2013 <- lm(hispanic_gap2012.2013 ~ percent_more_than_one_core_offering2012.2013 +
                                     percent_offering2012.2013 + partner_status2012.2013 + partner_num2012.2013 + participation_cat2012.2013 + participation_cat_binary2012.2013 
                                   + percent_cum_num_offering_participants2012.2013 + percent_cum_offering2012.2013 + percent_cum_num_more_than_one_core_offering_participants2012.2013
                                   + percent_core_offering2012.2013 + num_school_based_events2012.2013 + total_enroll2012.2013 + percent_minority_stud2012.2013
                                   + percent_hispanic_stud2012.2013 + percent_ell_stud2012.2013 + num_cum_school_based_events2012.2013 + hispanic_gap2011.2012, data = data)


summary(lm_hisp_2012.2013)

plot(data$hispanic_gap2011.2012, data$hispanic_gap_change2012.2013)
