from datetime import datetime, timedelta

d = datetime.now()

d2 = d + timedelta(minutes = 5)

print(d)
print(d2)

print(d > d2)
print(d < d2)