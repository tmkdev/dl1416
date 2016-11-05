#!/usr/bin/python
import datetime
import time
import logging

from dl1416 import DL1416

if __name__ == '__main__':
    display = DL1416(bl=23, cu=26, wr=12, ce=22)
    display2 = DL1416(bl=None, cu=26, wr=12, ce=24)

    display.initdisplay()
    display2.initdisplay()
    display.clear()
    display.writestring('ABCD')
    display2.writestring('EFGH')
    time.sleep(2)

    while True:
        display.writecur(0,True)
        display.writecur(1,True)
        display.writecur(2,True)
        display.writecur(3,True)
        display2.writecur(0,True)
        display2.writecur(1,True)
        display2.writecur(2,True)
        display2.writecur(3,True)
        time.sleep(0.5)
        display.writecur(0,False)  
        display.writecur(1,False)  
        display.writecur(2,False)  
        display.writecur(3,False)  
        display2.writecur(0,False)  
        display2.writecur(1,False)  
        display2.writecur(2,False)  
        display2.writecur(3,False)  
        time.sleep(1)
