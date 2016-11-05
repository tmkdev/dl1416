#!/usr/bin/python
import datetime
import time

from dl1416 import DL1416

""" datapins = [19, 15, 13, 11, 7, 5, 3], 
                addresspins = [18, 16], 
                ce = 22, 
                wr = 24, 
                cu = 26, 
                bl=None)"""


if __name__ == '__main__':
    display = DL1416(bl=23, wr=12, ce=22)
    display2 = DL1416(bl=None, wr=12, ce=24)

    display.initdisplay()
    display2.initdisplay()
    display.clear()
    display.writestring('TIME')
    display2.writestring('CLOK')
    time.sleep(2)

    ds = ''


    while True:
        if datetime.datetime.now().strftime("%I%M")<>ds: 
            ds=datetime.datetime.now().strftime("%I%M")
            display.writestring(ds)

	    secs=datetime.datetime.now().strftime("%S")
	    display2.writestring(':{0} '.format(secs))
        time.sleep(.5)
