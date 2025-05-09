'''Digital Current time using python'''
import time
import datetime


print("The Current time ---------")
while True:
    Current_time = datetime.datetime.now()
    time.sleep(1)
    print("\r", Current_time.strftime("%H:%M:%S"),end=" ",flush=True) 