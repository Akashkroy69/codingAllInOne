import datetime
# You can create date and time objects using the datetime class constructor. For example:
# Current date and time
current_datetime = datetime.datetime.now()

# Specific date
specific_date = datetime.datetime(2023, 9, 10)

# Specific time
specific_time = datetime.time(14, 30)
print("=============")
print(current_datetime)
print(specific_date)
print(specific_time)
print("=============")
# You can format date and time objects as strings using the strftime method. For example:
formatted_date = current_datetime.strftime("%Y-%m-%d")
formatted_time = current_datetime.strftime("%H:%M:%S")
print(formatted_date)
print(formatted_time)
print("=============")

# Date Arithmetic: You can perform arithmetic operations on dates and times. For example:
# from datetime import timedelta

# # Add 1 day to a date
# new_date = specific_date + timedelta(days=1)

# # Subtract 2 hours from a time
# new_time = specific_time - timedelta(hours=2)
print("=============")

import datetime



x=datetime.datetime.now()


print(x)


import time
 

obj = time.localtime()
print("local Time: ",obj)


t = time.asctime(obj)
print(t)
print("==================================================")
import calendar
# Display a calendar for September 2023
print(calendar.month(2023, 9))

# Display a calendar for the year 2023
print(calendar.calendar(2023))

# Get the day of the week (0 = Monday, 6 = Sunday) for September 10, 2023
day_of_week = calendar.weekday(2023, 9, 10)
print(day_of_week)
# Check if the year 2024 is a leap year
is_leap = calendar.isleap(2024)
print("===============")
date_string = "2023-09-10"
parsed_date = datetime.datetime.strptime(date_string, "%Y-%m-%d")


from datetime import timedelta

# Add 1 day to a date
new_date = specific_date + timedelta(days=1)

# Subtract 2 hours from a time
new_time = specific_time - timedelta(hours=2)
print(new_time)


