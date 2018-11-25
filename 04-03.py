from datetime import datetime, timedelta
import calendar

now = datetime.now()

testDate = now + timedelta(days=2)
myFirstdays = now - timedelta(weeks=3)

print(testDate.date())
print(myFirstdays.date())

if testDate > myFirstdays:
    print('Comparison works')

cal = calendar.month(2018, 11)
print(cal)

cal2 = calendar.weekday(2018, 11, 12)
print(cal2)
