import datetime

from datetime import date, timedelta
from datetime import datetime
from datetime import time


# currentTime = datetime.now()
currentTime = datetime.today()
print(f"Current Time : {currentTime}")
print(f"Current Year : {currentTime.year}")
print(f"Current Month : {currentTime.month}")
print(f"Current Time CTime : {currentTime.ctime()}")
print(f"Current Year : {datetime.strftime(currentTime, '%Y')}")
print(f"Current Date : {datetime.strftime(currentTime, '%x')}")
print(f"Current Day : {datetime.strftime(currentTime, '%d')}")



dateVal = '21 April 2025 hour 10:15:42'
dt = datetime.strptime(dateVal, '%d %B %Y hour %H:%M:%S')
print(f"Date time value : {dt}")



birthday = datetime(2025, 7, 16)
birthdayTimestamp = datetime.timestamp(birthday)
print(f"Birthday : {birthday}")
print(f"Birthday Timestamp : {birthdayTimestamp}")
print(f"Birthday Timestamp to Date : {datetime.fromtimestamp(birthdayTimestamp)}")


currentDateValue = datetime.now()
result = currentDateValue + timedelta(days=10)
print(f"Time delta result : {result}")