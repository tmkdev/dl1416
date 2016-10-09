import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)


class DL1416(object):
    _DISPLAYWIDTH=4

    def __init__(self, datapins = [19, 15, 13, 11, 7, 5, 3], addresspins = [18, 16], ce = 22, wr = 24, cu = 26):
        self.datapins = datapins
        self.addresspins = addresspins
        self.ce = ce
        self.wr = wr
        self.cu = cu
	
    def initdisplay(self):
        for pin in self.datapins:
            GPIO.setup(pin, GPIO.OUT)
        for pin in self.addresspins:
            GPIO.setup(pin, GPIO.OUT)
        for pin in [ self.ce, self.wr, self.cu ]:
            GPIO.setup(pin, GPIO.OUT)
  
        GPIO.output([ self.wr, self.ce, self.cu ], (GPIO.HIGH, GPIO.HIGH, GPIO.HIGH))

    def clear(self):
    	self.writestring(' ' * self._DISPLAYWIDTH)

    def writestring(self, text):
        for pos, char in enumerate(text[0:self._DISPLAYWIDTH][::-1]):
            self.writechar(pos, char)

    def writechar(self, pos, char):
        address = [int(x) for x in list('{0:0b}'.format(pos+128))]
        char=[int(x) for x in list('{0:0b}'.format(128+ord(char)))]
        GPIO.output(self.addresspins, address[-2:])
        GPIO.output(self.ce, GPIO.LOW)    
        GPIO.output([ self.wr, self.cu], (GPIO.LOW, GPIO.HIGH))

        GPIO.output(self.datapins, char[-7:])
        GPIO.output(self.wr, GPIO.HIGH)    
        GPIO.output([ self.ce, self.cu ], (GPIO.HIGH,GPIO.HIGH) )


