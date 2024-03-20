# Import required libraries
import calendar

# Create a text calendar
cal = calendar.TextCalendar(calendar.SUNDAY) # Set the first day of the week to Sunday

# Print the calendar for the year 2024
print(cal.formatyear(2024))
