from dl1416 import *
import datetime
import time

dl = DualDL()

if __name__ == '__main__':
    while True:
        if datetime.datetime.now().second % 2 == 0:
            dl.writestring(datetime.datetime.now().strftime('%H:%M:%S'))
        else:
            dl.writestring(datetime.datetime.now().strftime('%H %M %S'))
        time.sleep(.1)    

