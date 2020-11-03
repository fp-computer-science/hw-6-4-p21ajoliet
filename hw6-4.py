#Author: ALJ (AMDG) 10/30/20

import calendar
import time

#Question 1
calendar.TextCalendar().pryear(2020)

#Question 2
calendar.TextCalendar(6).pryear(2020)

#Question 3
print(calendar.month(2020, 9))

#Question 4
#calendar.LocaleTextCalendar(6, "SPANISH").pryear(2020)
#calendar.LocaleTextCalendar(6, "ENGLISH").pryear(2020)
#calendar.LocaleTextCalendar(6, "MARATHI").pryear(2020)
##calendar.LocaleTextCalendar(6, "PIG LATIN").pryear(2020)

#Question 5
print(calendar.isleap(2019))
print(calendar.isleap(2020))
print(calendar.isleap(2016))
#This returns true or false, true if it is a leap year and false if it isn't.
#It expects the year as an input