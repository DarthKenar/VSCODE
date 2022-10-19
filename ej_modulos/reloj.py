import datetime as dt
import time as t
import os 

while True:
    
    print(f"{dt.datetime.now().hour}:{dt.datetime.now().minute}:{dt.datetime.now().second}")
    t.sleep(1)
    os.system("cls")