year = 2024

for month in range(1, 13):
    print(f"Month {month} ({calendar.month_name[month]}):")
    for date in cal.itermonthdates(year, month):
        if date.month == month:
            print(date)


