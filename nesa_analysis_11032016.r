data <- read.csv(file.choose())

library(Hmisc)

names(data)

table(data$partner_status, data$entity)
table(data$partner_num)

###i am starting with nesa_5.csv

describe(data$gap_math_black_score[data$partner_status=="NON" & data$school_year == '2014-2015'])
describe(data$gap_math_black_score[data$partner_status=="PARTNER" & data$school_year == '2014-2015'])

describe(data$gap_math_black_score[data$partner_num==0 & data$school_year == '2014-2015'])
describe(data$gap_math_black_score[data$partner_num == 1 & data$school_year == '2014-2015'])
describe(data$gap_math_black_score[data$partner_num == 2 & data$school_year == '2014-2015'])
describe(data$gap_math_black_score[data$partner_num == 3 & data$school_year == '2014-2015'])

data$partner_ever = data$partner_num >= 1

table(data$partner_status)

describe(data$gap_math_black_score[data$partner_ever == FALSE & data$school_year == '2014-2015'])
describe(data$gap_math_black_score[data$partner_ever == TRUE & data$school_year == '2014-2015'])

hist(data$gap_math_black_score[data$partner_num==0])

library(car)

qqnorm(data$gap_math_black_score[data$partner_num==0])
qqnorm(data$gap_math_black_score[data$partner_num==1])
qqnorm(data$gap_math_black_score[data$partner_num==2])
qqnorm(data$gap_math_black_score[data$partner_num==3])
qqnorm(data$gap_math_black_score[data$partner_ever==TRUE])
qqnorm(data$gap_math_black_score[data$partner_ever==FALSE])

fit <- aov(gap_math_black_score ~ partner_ever, data=data)
summary(fit)

describe(data$gap_math_black_score[data$school_year == '2014-2015'])
describe(data$gap_math_black_score[data$school_year == '2013-2014'])
describe(data$gap_math_black_score[data$school_year == '2012-2013'])
describe(data$gap_math_black_score[data$school_year == '2011-2012'])


