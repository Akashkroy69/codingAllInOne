import datetime
# from datetime import datetime

now = datetime.datetime.now()
print(now)

print("Year:", now.year)  
print("Month:", now.month)  
print("Day:", now.day)  
print("Hour:", now.hour)  
print("Minute:", now.minute)  
print("Second:", now.second)  
print("Microsecond:", now.microsecond)  

# formatting
formatted_date = now.strftime("%d-%M-%Y %I:%M:%S %p")  
print(formatted_date)  # Output: 09-03-2025 12:34:56

# difference between two dates
date1 = datetime.datetime(2025, 5, 15)  
date2 = datetime.datetime(2025, 3, 9)  
difference = date1 - date2  
print("Difference:", difference.days, "days")  


weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
today = datetime.datetime.now()
print("Today is:", weekdays[today.weekday()])  
print("Today is:", today.strftime("%A")) 
print(today.weekday())






# print(x.year)
# print(x.strftime("%A"))
# print(x.strftime("%B"))
# print(x.strftime("%c"))

# # Creating a date object
# y = datetime.datetime(2021, 7, 12)
# print(y)