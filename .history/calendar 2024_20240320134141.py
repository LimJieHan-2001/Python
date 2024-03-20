>>> import icalendar
>>> path_to_ics_file = "src/icalendar/tests/calendars/example.ics"
>>> with open(path_to_ics_file) as f:
...     calendar = icalendar.Calendar.from_ical(f.read())
>>> for event in calendar.walk('VEVENT'):
...     print(event.get("SUMMARY"))
New Year's Day
Orthodox Christmas
International Women's Day