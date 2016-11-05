import time 
import RPi.GPIO as GPIO
import logging

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

bl=23

GPIO.setup(bl, GPIO.OUT)

p = GPIO.PWM(bl, 1000)
p.start(0)
while True:
    for dc in range(0, 101, 2):
        p.ChangeDutyCycle(dc)
        time.sleep(0.03)
    for dc in range(100, -1, -2):
        p.ChangeDutyCycle(dc)
        time.sleep(0.03)
