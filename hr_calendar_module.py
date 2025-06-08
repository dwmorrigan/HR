# Take the date and return the day of the week (in all caps)
# The calendar module is impressive - this was much easier than I expected

import calendar

weekdays = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
m, d, y = map(int, input().strip().split())

dd = calendar.weekday(y, m, d)

print(weekdays[dd].upper())