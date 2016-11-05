import time 
import RPi.GPIO as GPIO
import logging

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)


class DL1416(object):
    _DISPLAYWIDTH=4

    def __init__(self, 
                datapins = [19, 15, 13, 11, 7, 5, 3], 
                addresspins = [18, 16], 
                ce = 22, 
                wr = 24, 
                cu = 26, 
                bl=None):
        self.datapins = datapins
        self.addresspins = addresspins
        self.ce = ce
        self.wr = wr
        self.cu = cu
        self.bl = bl
        self.text = [ ' ' ] * DL1416._DISPLAYWIDTH
        self.dutycycle=100	
        self.pwmpin = None
        
    def initdisplay(self):
        for pin in self.datapins:
            GPIO.setup(pin, GPIO.OUT)
        for pin in self.addresspins:
            GPIO.setup(pin, GPIO.OUT)
        for pin in [ self.ce, self.wr, self.cu ]:
            GPIO.setup(pin, GPIO.OUT)
  
        if self.bl:
            GPIO.setup(self.bl, GPIO.OUT)
            self.pwmpin=GPIO.PWM(self.bl, 1000)
            self.pwmpin.start(self.dutycycle)

        GPIO.output([ self.wr, self.ce, self.cu ], (GPIO.HIGH, GPIO.HIGH, GPIO.HIGH))

        logging.warning("DLx416 Initialized")

    def clear(self):
    	self.writestring(' ' * self._DISPLAYWIDTH)
        logging.info("DLx416 Cleared")

    def setBrightness(self, dutycycle):
        if self.bl:
            self.pwmpin.ChangeDutyCycle(dutycycle)
            self.dutycycle=dutycycle

    def dimDisplay(self, setpoint=0, speed=0.03):
        if self.dutycycle > setpoint:
            for dc in range(self.dutycycle, setpoint-1, -2):
                self.setBrightness(dc)
                time.sleep(speed)
            self.dutycycle=setpoint

    def undimDisplay(self, setpoint=100, speed=0.03):
        if self.dutycycle < setpoint:
            for dc in range(self.dutycycle, setpoint+1, 2):
                self.setBrightness(dc)
                time.sleep(0.03)
            self.dutycycle=setpoint

    def writestring(self, text):
        for pos, char in enumerate(text[0:self._DISPLAYWIDTH][::-1]):
            self.writechar(pos, char)

    def writecur(self, pos, enable):
        logging.info("Setting cursor {0} to {1}".format(pos, enable))
        address = [int(x) for x in list('{0:0b}'.format(pos+128))]
        data = [ False, False, False, False, False, False, enable]
        GPIO.output(self.addresspins, address[-2:])
        GPIO.output(self.ce, GPIO.LOW)    
        GPIO.output(self.datapins, data)
        GPIO.output([ self.wr, self.cu], (GPIO.LOW, GPIO.LOW))
        pass
        pass
        GPIO.output(self.wr, GPIO.HIGH)    
        GPIO.output([ self.ce, self.cu ], (GPIO.HIGH,GPIO.HIGH) )

        if not enable:
            self.writechar(pos, self.text[pos])

    def writechar(self, pos, char):
        self.text[pos] = char
        address = [int(x) for x in list('{0:0b}'.format(pos+128))]
        char=[int(x) for x in list('{0:0b}'.format(128+ord(char)))]
        GPIO.output(self.addresspins, address[-2:])
        GPIO.output(self.ce, GPIO.LOW)    
        GPIO.output(self.datapins, char[-7:])

        GPIO.output([ self.wr, self.cu], (GPIO.LOW, GPIO.HIGH))
        pass
        pass
        GPIO.output(self.wr, GPIO.HIGH)    
        GPIO.output([ self.ce, self.cu ], (GPIO.HIGH,GPIO.HIGH) )

        logging.info('Display contents-> {0}'.format(self.text[::-1]))


class DualDL(object):
    _DISPLAYWIDTH=8

    def __init__(self,
                datapins = [19, 15, 13, 11, 7, 5, 3],
                addresspins = [18, 16],
                ce0 = 22,
                ce1 = 24,
                wr = 12,
                cu = 26,
                bl = 23):

        self.displaycontents = ' ' * 8
        self.displays = [
            DL1416(datapins=datapins,
                   addresspins=addresspins,
                   ce = ce0,
                   wr = wr,
                   cu = cu,
                   bl = bl),
            DL1416(datapins=datapins,
                   addresspins=addresspins,
                   ce = ce1,
                   wr = wr,
                   cu = cu,
                   bl = None),
        ]

        for display in self.displays:   
            display.initdisplay()

    def clear(self):
        self.displaystring('')


    def setbrightness(self, dutycycle):
        self.displays[0].setBrightness(dutycycle)

    def writestring(self, text):
        text = ' ' * self._DISPLAYWIDTH + text
        displaytext = text[-self._DISPLAYWIDTH:]
        self.displaytext = displaytext

        logging.info("Display text: {0}".format(self.displaytext))

        self.displays[0].writestring(displaytext[0:4])
        self.displays[1].writestring(displaytext[4:8])
