import random
from datetime import datetime, timedelta

# Define the range of dates between which you want to generate a random date and time
start_date = datetime(2023, 1, 1)
end_date = datetime(2023, 12, 31)

# Calculate the time difference between the start and end dates
time_difference = end_date - start_date
print("Time Difference: ",time_difference)

# Generate a random number of seconds within the time difference
random_seconds = random.randint(0, time_difference.total_seconds())

# Create a new datetime by adding the random number of seconds to the start date
random_datetime = start_date + timedelta(seconds=random_seconds)

print("Random Date and Time:", random_datetime)
