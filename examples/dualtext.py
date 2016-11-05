from dl1416 import *
import time
import os

dl = DualDL()

if __name__ == '__main__':
    while True:
        loads = os.getloadavg()
        dl.writestring('CPU {:4.2f}'.format(loads[0]))
        time.sleep(.5)    

