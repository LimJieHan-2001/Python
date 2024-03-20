import calendar

# Create a Text Calendar for the year 2024
cal = calendar.TextCalendar(calendar.SUNDAY)  # Set the first day of the week (Sunday)

# Display the calendar for the entire year
year = 2024
print(f"Calendar for {year}:\n")
for month in range(1, 13):
    month_name = calendar.month_name[month]
    print(f"{month_name} {year}")
    print(cal.formatmonth(year, month))
    print("\n")
