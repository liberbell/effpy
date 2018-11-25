from datetime import datetime, timedelta

now = datetime.now()

testDate = now + timedelta(days=2)
myFirstdays = now - timedelta(weeks=3)

print(testDate)
print(myFirstdays)
