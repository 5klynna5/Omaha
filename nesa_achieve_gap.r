
library(e1071)
library(ggplot2)
library(plyr)
library(gridExtra)
library(Hmisc)

###here load in file from 'analysis by demographic' folder
data <- read.csv(file.choose())

names(data)

###a higher gap means non-white students are achieving at higher rate of white students

##a higher / more positive gap means that this year non-white students are achieving at a high rate of white students than last year

###a positive correlation between percent participation and gap or gap change is a positive thing

##correlation tables
cor_gap_change2014.2015 <- cor(data[c("percent_offering2014.2015", "percent_more_than_one_core_offering2014.2015", "num_school_based_events2014.2015", "partner_num2014.2015", "hispanic_gap_change2014.2015", "black_gap_change2014.2015", "amer_indian_gap_change2014.2015", "pac_islander_gap_change2014.2015", "multi_racial_gap_change2014.2015", "asian_gap_change2014.2015")], use = "pairwise.complete.obs")
cor_gap_change2014.2015

cor_gap2014.2015 <- cor(data[c("percent_offering2014.2015", "percent_more_than_one_core_offering2014.2015", "num_school_based_events2014.2015", "partner_num2014.2015", "hispanic_gap2014.2015", "black_gap2014.2015", "amer_indian_gap2014.2015", "pac_islander_gap2014.2015", "multi_racial_gap2014.2015", "asian_gap2014.2015")], use = "pairwise.complete.obs")
cor_gap2014.2015

#####linear models

###hispanic students

########percent offering

lm_hispanic_gap_change2012.2013 <- lm(hispanic_gap_change2012.2013 ~ percent_offering2012.2013 , data = data)
summary(lm_hispanic_gap_change2012.2013)

ggplot(data = data, aes(x = percent_offering2012.2013, y = hispanic_gap_change2012.2013)) +
  geom_point() +
  geom_smooth(method = "lm")

lm_hispanic_gap_change2013.2014 <- lm(hispanic_gap_change2013.2014 ~ percent_offering2013.2014 , data = data)
summary(lm_hispanic_gap_change2013.2014)

ggplot(data = data, aes(x = percent_offering2013.2014, y = hispanic_gap_change2013.2014)) +
  geom_point() +
  geom_smooth(method = "lm")

lm_hispanic_gap_change2014.2015 <- lm(hispanic_gap_change2014.2015 ~ percent_offering2014.2015 , data = data)
summary(lm_hispanic_gap_change2014.2015)

ggplot(data = data, aes(x = percent_offering2014.2015, y = hispanic_gap_change2014.2015)) +
  geom_point() +
  geom_smooth(method = "lm")

#############percent more than one core offering

lm_hispanic_gap_change2012.2013 <- lm(hispanic_gap_change2012.2013 ~ percent_more_than_one_core_offering2012.2013 , data = data)
summary(lm_hispanic_gap_change2012.2013)

ggplot(data = data, aes(x = percent_more_than_one_core_offering2012.2013, y = hispanic_gap_change2012.2013)) +
  geom_point() +
  geom_smooth(method = "lm")

lm_hispanic_gap_change2013.2014 <- lm(hispanic_gap_change2013.2014 ~ percent_more_than_one_core_offering2013.2014 , data = data)
summary(lm_hispanic_gap_change2013.2014)

ggplot(data = data, aes(x = percent_more_than_one_core_offering2013.2014, y = hispanic_gap_change2013.2014)) +
  geom_point() +
  geom_smooth(method = "lm")

lm_hispanic_gap_change2014.2015 <- lm(hispanic_gap_change2014.2015 ~ percent_more_than_one_core_offering2014.2015 , data = data)
summary(lm_hispanic_gap_change2014.2015)

ggplot(data = data, aes(x = percent_more_than_one_core_offering2014.2015, y = hispanic_gap_change2014.2015)) +
  geom_point() +
  geom_smooth(method = "lm")

###partner num 2014-2015

lm_hispanic_gap_change2014.2015 <- lm(hispanic_gap_change2014.2015 ~ partner_num2014.2015 , data = data)
summary(lm_hispanic_gap_change2014.2015)

ggplot(data = data, aes(x = partner_num2014.2015, y = hispanic_gap_change2014.2015)) +
  geom_point() +
  geom_smooth(method = "lm")

###playing with this model
lm_hispanic_gap_change2014.2015 <- lm(hispanic_gap_change2014.2015 ~ percent_offering2014.2015 + partner_num2014.2015, data = data)
summary(lm_hispanic_gap_change2014.2015)


cor(data[c("hispanic_gap_change2014.2015", "percent_offering2012.2013", "percent_more_than_one_core_offering2012.2013", "percent_offering2013.2014", "percent_more_than_one_core_offering2013.2014","percent_offering2014.2015", "percent_more_than_one_core_offering2014.2015", "partner_num2014.2015", "percent_minority_stud2014.2015", "total_enroll2014.2015", "percent_ell_stud2014.2015", "percent_hispanic_stud2014.2015")], use = "pairwise.complete.obs")

###interesting here is that most sig correlation is participation in 2014-2015 in one offering (with gap change), but participating in previous years have positive correlation (not significant though)

ggplot(data = data, aes(x = percent_offering2014.2015, y = hispanic_gap_change2014.2015)) +
  geom_point() +
  geom_smooth(method = "lm")

lm_black_gap_change2014.2015 <- lm(black_gap_change2014.2015 ~ percent_more_than_one_core_offering2013.2014 + percent_more_than_one_core_offering2014.2015 + percent_black_stud2014.2015, data = data)
summary(lm_black_gap_change2014.2015)

cor(data[c("black_gap_change2014.2015", "percent_offering2013.2014", "percent_more_than_one_core_offering2013.2014","percent_offering2014.2015", "percent_more_than_one_core_offering2014.2015", "partner_num2014.2015", "percent_white_stud2014.2015", "total_enroll2014.2015", "percent_ell_stud2014.2015", "percent_black_stud2014.2015")], use = "pairwise.complete.obs")

###interestingly enough here, the number of black students has highest negative correlation and number ell students highest positive correlation
###black students
########percent offering

lm_black_gap_change2012.2013 <- lm(black_gap_change2012.2013 ~ percent_offering2012.2013 , data = data)
summary(lm_black_gap_change2012.2013)

ggplot(data = data, aes(x = percent_offering2012.2013, y = black_gap_change2012.2013)) +
  geom_point() +
  geom_smooth(method = "lm")

lm_black_gap_change2013.2014 <- lm(black_gap_change2013.2014 ~ percent_offering2013.2014 , data = data)
summary(lm_black_gap_change2013.2014)

ggplot(data = data, aes(x = percent_offering2013.2014, y = black_gap_change2013.2014)) +
  geom_point() +
  geom_smooth(method = "lm")

lm_black_gap_change2014.2015 <- lm(black_gap_change2014.2015 ~ percent_offering2014.2015 , data = data)
summary(lm_black_gap_change2014.2015)

ggplot(data = data, aes(x = percent_offering2014.2015, y = black_gap_change2014.2015)) +
  geom_point() +
  geom_smooth(method = "lm")

#############percent more than one core offering

lm_black_gap_change2012.2013 <- lm(black_gap_change2012.2013 ~ percent_more_than_one_core_offering2012.2013 , data = data)
summary(lm_black_gap_change2012.2013)

ggplot(data = data, aes(x = percent_more_than_one_core_offering2012.2013, y = black_gap_change2012.2013)) +
  geom_point() +
  geom_smooth(method = "lm")

lm_black_gap_change2013.2014 <- lm(black_gap_change2013.2014 ~ percent_more_than_one_core_offering2013.2014 , data = data)
summary(lm_black_gap_change2013.2014)

ggplot(data = data, aes(x = percent_more_than_one_core_offering2013.2014, y = black_gap_change2013.2014)) +
  geom_point() +
  geom_smooth(method = "lm")

lm_black_gap_change2014.2015 <- lm(black_gap_change2014.2015 ~ percent_more_than_one_core_offering2014.2015 , data = data)
summary(lm_black_gap_change2014.2015)

ggplot(data = data, aes(x = percent_more_than_one_core_offering2014.2015, y = black_gap_change2014.2015)) +
  geom_point() +
  geom_smooth(method = "lm")

###partner num 2014-2015

lm_black_gap_change2014.2015 <- lm(black_gap_change2014.2015 ~ partner_num2014.2015 , data = data)
summary(lm_black_gap_change2014.2015)

ggplot(data = data, aes(x = partner_num2014.2015, y = black_gap_change2014.2015)) +
  geom_point() +
  geom_smooth(method = "lm")

lm_black_gap_change2014.2015 <- lm(black_gap_change2014.2015 ~ percent_offering2014.2015 + partner_num2014.2015, data = data)
summary(lm_black_gap_change2014.2015)

ggplot(data = data, aes(x = percent_offering2014.2015, y = black_gap_change2014.2015)) +
  geom_point() +
  geom_smooth(method = "lm")

####mutli-racial students

########percent offering

lm_multi_racial_gap_change2012.2013 <- lm(multi_racial_gap_change2012.2013 ~ percent_offering2012.2013 , data = data)
summary(lm_multi_racial_gap_change2012.2013)

ggplot(data = data, aes(x = percent_offering2012.2013, y = multi_racial_gap_change2012.2013)) +
  geom_point() +
  geom_smooth(method = "lm")

lm_multi_racial_gap_change2013.2014 <- lm(multi_racial_gap_change2013.2014 ~ percent_offering2013.2014 , data = data)
summary(lm_multi_racial_gap_change2013.2014)

ggplot(data = data, aes(x = percent_offering2013.2014, y = multi_racial_gap_change2013.2014)) +
  geom_point() +
  geom_smooth(method = "lm")

lm_multi_racial_gap_change2014.2015 <- lm(multi_racial_gap_change2014.2015 ~ percent_offering2014.2015 , data = data)
summary(lm_multi_racial_gap_change2014.2015)

ggplot(data = data, aes(x = percent_offering2014.2015, y = multi_racial_gap_change2014.2015)) +
  geom_point() +
  geom_smooth(method = "lm")

#############percent more than one core offering

lm_multi_racial_gap_change2012.2013 <- lm(multi_racial_gap_change2012.2013 ~ percent_more_than_one_core_offering2012.2013 , data = data)
summary(lm_multi_racial_gap_change2012.2013)

ggplot(data = data, aes(x = percent_more_than_one_core_offering2012.2013, y = multi_racial_gap_change2012.2013)) +
  geom_point() +
  geom_smooth(method = "lm")

lm_multi_racial_gap_change2013.2014 <- lm(multi_racial_gap_change2013.2014 ~ percent_more_than_one_core_offering2013.2014 , data = data)
summary(lm_multi_racial_gap_change2013.2014)

ggplot(data = data, aes(x = percent_more_than_one_core_offering2013.2014, y = multi_racial_gap_change2013.2014)) +
  geom_point() +
  geom_smooth(method = "lm")

lm_multi_racial_gap_change2014.2015 <- lm(multi_racial_gap_change2014.2015 ~ percent_more_than_one_core_offering2014.2015 , data = data)
summary(lm_multi_racial_gap_change2014.2015)

ggplot(data = data, aes(x = percent_more_than_one_core_offering2014.2015, y = multi_racial_gap_change2014.2015)) +
  geom_point() +
  geom_smooth(method = "lm")

###partner num 2014-2015

lm_multi_racial_gap_change2014.2015 <- lm(multi_racial_gap_change2014.2015 ~ partner_num2014.2015 , data = data)
summary(lm_multi_racial_gap_change2014.2015)

ggplot(data = data, aes(x = partner_num2014.2015, y = multi_racial_gap_change2014.2015)) +
  geom_point() +
  geom_smooth(method = "lm")

lm_multi_racial_gap_change2014.2015 <- lm(multi_racial_gap_change2014.2015 ~ percent_offering2014.2015 + partner_num2014.2015, data = data)
summary(lm_multi_racial_gap_change2014.2015)

ggplot(data = data, aes(x = percent_offering2014.2015, y = multi_racial_gap_change2014.2015)) +
  geom_point() +
  geom_smooth(method = "lm")