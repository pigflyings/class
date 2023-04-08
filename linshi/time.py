import time
curTime = time.time()
totalseconds =int(curTime)
cursecond=totalseconds%60
totalMinutes=totalseconds//60
curMinute=totalMinutes%60
totalhours=totalMinutes//60
curHour=totalhours%24 +8
print("s=",curTime)
print(curHour,"时",curMinute,"分",cursecond,"秒")