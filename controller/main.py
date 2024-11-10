import datetime

now = datetime.datetime.now()
dt1 = now.strftime("%Y-%m-%d %H:%M:%S")
dt2 = datetime.datetime(2024, 1, 1, 12, 00, 1)
dt3 = datetime.date.todaty()
print(now)
print(dt1)
print(dt2)
print(dt3)
