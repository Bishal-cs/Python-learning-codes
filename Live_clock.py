import time 
import datetime

print("Current Clock")
while True:
    current_time = datetime.datetime.now()
    print("\r",current_time.strftime("%H:%M:%S"),end="",flush=True)
    time.sleep(1)
