import datetime as dt

now = dt.datetime.now()
print(now)
print(now.year)
print(now.month)
print(now.day)
print(now.weekday())

date_of_birth = dt.datetime(year=2000, month=5, day=20)
print(date_of_birth)