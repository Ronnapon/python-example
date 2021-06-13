# Date Time
from datetime import datetime, timedelta
import time

# Time Stamp
start = time.time()
end = time.time()
duration = end - start
print(duration)

#dt1 = datetime(2018, 1, 1) + timedelta(1)
dt1 = datetime(2018, 1, 1) + timedelta(days=1, seconds=1)
print(dt1)
dt2 = datetime.now()
print(dt2)
dt = datetime.strptime("2018/01/01", "%Y/%m/%d")
print(dt)
dt = datetime.fromtimestamp(time.time())
print(dt)

print(f"{dt.year}/{dt.month}")
print(dt.strftime("%Y/%m"))

print(dt1 > dt2)

duration = dt2-dt1
print(duration)
print("days", duration.days)
print("seconds", duration.seconds)
print("total seconds", duration.total_seconds())
