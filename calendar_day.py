import calendar

day_of_the_week = list(calendar.day_name)
print(day_of_the_week)

import random

day_wise_temp_celcius = {day:random.randint(20, 30) for day in day_of_the_week}

print(day_wise_temp_celcius)

day_wise_temp_faren = {day:temp*1.8 + 32 for (day, temp) in day_wise_temp_celcius.items()}
print(day_wise_temp_faren)