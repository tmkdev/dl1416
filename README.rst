======
dl1416
======

Library for driving DL1416/DL2416 LED arrays on Raspberry Pi/RPi.GPIO supported dev boards

Installation
============

pip install dl1416

Example Usage
=============

from dl1416 import DL1416

dl = DL1416()    

dl.initdisplay()
dl.clear()

dl.writestring('HELO')


DL1416 default pin connections:
(Using BOARD pin numbers)

Altenate pins can be passed into the constructor

datapins = [19, 15, 13, 11, 7, 5, 3]
addresspins = [18, 16]
ce = 22
wr = 24
cu = 26




