from datetime import date, timedelta

sundays = 0
current_date = date(1901, 1, 1)

while current_date.year < 2001:
    if current_date.weekday() == 6 and current_date.day == 1:
        sundays += 1

    current_date += timedelta(days=1)

print(sundays)