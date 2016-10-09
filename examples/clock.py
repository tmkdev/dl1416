#!/usr/bin/python
import datetime
import time

from dl1416 import DL1416


if __name__ == '__main__':
    display = DL1416()

    display.initdisplay()
    display.clear()
    display.writestring('TIME')
    time.sleep(2)

    ds = datetime.datetime.now().strftime("%I%M")

    display.writestring(ds)

    while True:
        if datetime.datetime.now().strftime("%I%M")<>ds: 
            ds=datetime.datetime.now().strftime("%I%M")
            display.writestring(ds)

        time.sleep(.1)
