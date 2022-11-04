import time
import datetime



print(time.time())
print(time.strftime("%Y-%m-%d %H:%M:%S"))
print(time.strptime("2022-11-04 10:43:30","%Y-%m-%d %H:%M:%S"))
lo_time = time.localtime()
print(lo_time.tm_year)

print(datetime.datetime.now())
print(datetime.datetime.now()+datetime.timedelta(days=3))