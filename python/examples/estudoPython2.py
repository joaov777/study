#!/usr/bin/env python3


# Using datetime functions and different printing formats

from datetime import datetime, timedelta

current_date = datetime.now()

print("Today is: {}".format(str(current_date)))
print(f"The day is: {str(current_date.day)}")
print("The month is: " + str(current_date.month))
print("The year is: " + str(current_date.year))

print("The hour is: " + str(current_date.hour))
print("The minute is: " + str(current_date.minute))

one_day = timedelta(days=1)

yesterday = current_date - one_day

print("Yesterday was: " + str(yesterday.day))

# Interesting if statement

name = input("What is your name? ").lower()

if name in ('carlos','andre', 'marcelo'):
    print("Brazillian")
elif name in ('andrew','mike','katherine'):
    print("American")
else:
    print("The name is exotic")


#Conditionals with booleans

grade = float(8.0)
flag = False

if grade >= 6.0 and grade <= 10.0:
    flag = True
elif grade < 6.0:
    flag = False

if flag:
    print("If this is printed, flag is True. The student has passed! :) ")

if not flag:
    print("If this is printed, flag is False. The student has not passed! :( ")


# Working with percentages

tax_rate = .43
price = float(200)

final_price_after_tax = price+(price*tax_rate)

if tax_rate > .50:
    print("They have charged a lot! --> " + str(final_price_after_tax))
else:
    print("They have not charged much! --> " + str(final_price_after_tax))
