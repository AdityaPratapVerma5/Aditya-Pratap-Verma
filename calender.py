import calendar
def create_calendar(year, month):
# Creating a Text Calendar instance
cal = calendar.TextCalendar(calendar.SUNDAY)
# Format and print the calendar
calendar_text = cal.formatmonth(year, month)
print(calendar_text)
# Example usage:
year = 2024
month = 4
create_calendar(year, month)