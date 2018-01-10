library(e1071)
library(ggplot2)
library(plyr)
library(gridExtra)
library(Hmisc)
library(car)

###here load in file from 'analysis by demographic' folder
data <- read.csv(file.choose())

###a higher gap means non-white students are achieving at higher rate of white students

##a higher / more positive gap means that this year non-white students are achieving at a high rate of white students than last year

###a positive correlation between percent participation and gap or gap change is a positive thing



###playing with this model
lm_hispanic_gap_change2014.2015 <- lm(hispanic_gap_change2014.2015 ~ percent_more_than_one_core_offering2014.2015, data = data)
summary(lm_hispanic_gap_change2014.2015)

ggplot(data = data, aes(x = percent_offering2014.2015, y = hispanic_gap_change2014.2015)) +
  geom_point() +
  geom_smooth(method = "lm")

qqnorm(data$hispanic_gap_change2014.2015,main="Normal Q-Q Plot")
qqline(data$hispanic_gap_change2014.2015)



plot(density(resid(lm_hispanic_gap_change2014.2015)), xlab = "Model Residuals")
mean(resid(lm_hispanic_gap_change2014.2015))
sd(resid(lm_hispanic_gap_change2014.2015))

plot(x = data$percent_more_than_one_core_offering2014.2015, y = rstandard(lm_hispanic_gap_change2014.2015),  
     xlab="participation", 
     ylab="Studentized Residuals")
abline(h = 0)
abline(h = -2, lty = "dotted")
abline(h = 2, lty = "dotted")

plot(data$hispanic_gap_change2014.2015, data$percent_offering2014.2015)
abline = 

cor(data[c("hispanic_gap_change2014.2015", "percent_offering2012.2013", "percent_more_than_one_core_offering2012.2013", "percent_offering2013.2014", "percent_more_than_one_core_offering2013.2014","percent_offering2014.2015", "percent_more_than_one_core_offering2014.2015", "partner_num2014.2015", "percent_minority_stud2014.2015", "total_enroll2014.2015", "percent_ell_stud2014.2015", "percent_hispanic_stud2014.2015")], use = "pairwise.complete.obs")

### math_3 interesting here is that most sig correlation is participation in 2014-2015 in one offering (with gap change), but participating in previous years have positive correlation (not significant though)


lm_black_gap_change2013.2014 <- lm(black_gap_change2013.2014 ~ percent_offering2013.2014, data = data)
summary(lm_black_gap_change2013.2014)

plot(data$percent_offering2013.2014, data$black_gap_change2013.2014)

cor(data[c("black_gap_change2013.2014", "percent_offering2013.2014", "percent_more_than_one_core_offering2013.2014","percent_offering2013.2014", "percent_more_than_one_core_offering2013.2014", "partner_num2013.2014", "percent_white_stud2013.2014", "total_enroll2013.2014", "percent_ell_stud2013.2014", "percent_black_stud2013.2014")], use = "pairwise.complete.obs")

###math_3interestingly enough here, the number of black students has highest negative correlation and number ell students highest positive correlation