
data <- read.csv(file.choose())

table(data$partner_num2014.2015)

describe(data$hispanic_gap_change_total)

qqnorm(data$hispanic_gap_change_total,main="Normal Q-Q Plot partners")
hist(data$hispanic_gap_change_total)
plot(density(na.omit(data$hispanic_gap_change_total)))

never_partner=subset(data,partner_num2014.2015 == "0")
partner = subset(data,partner_num2014.2015 != "0")

data$ever_partner <- with(data,ifelse(partner_num2014.2015 == "0", "NO", "YES"))
data$two_partner <- with(data, ifelse((partner_num2014.2015 == "0" | partner_num2014.2015 == "1"), "NO", "YES"))

table(data$two_partner)
table(data$ever_partner)

table(never_partner$partner_num2014.2015)
table(partner$partner_num2014.2015)

hist(partner$hispanic_gap_total_change)
plot(density(na.omit(partner$hispanic_gap_change_total),main="partners"))
boxplot(partner$hispanic_gap_change_total, horizontal=TRUE,main="partners")
qqnorm(partner$hispanic_gap_change_total,main="Normal Q-Q Plot partners")
qqline(partner$hispanic_gap_change_total)

hist(never_partner$hispanic_gap_change_total)
plot(density(na.omit(partner$hispanic_gap_change_total),main="never partners"))
boxplot(never_partner$hispanic_gap_change_total, horizontal=TRUE,main="never partners")
qqnorm(never_partner$hispanic_gap_change_total,main="Normal Q-Q Plot never partners")
qqline(never_partner$hispanic_gap_change_total)

t.test(data$hispanic_gap_change_total~data$two_partner)

t.test(data$black_gap_change_total~data$two_partner)

t.test(data$multi_racial_gap_change_total~data$two_partner)


