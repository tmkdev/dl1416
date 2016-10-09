#!/usr/bin/python
import os
import time
from dl1416 import DL1416


if __name__ == '__main__':
    dl = DL1416()    

    dl.initdisplay()
    dl.clear()

    while True:
        loads = os.getloadavg()
        dl.writestring('{:4.2f}'.format(loads[0]))
        time.sleep(0.1)   
