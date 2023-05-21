import RPi.GPIO as GPIO
import sys
from time import sleep
GPIO.setmode(GPIO.BCM)
dac=[26,19,13,6,5,11,9,10]
GPIO.setup(dac, GPIO.OUT)

def decimal2binary(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

try:
    T=input()
    if not T.isdigit():
        print('T must be float')
    else:
        while('True'):
            t=float(T)/256/2
            for i in range (256):
                GPIO.output(dac,decimal2binary(i))
                sleep(t)
            for i in range (255,-1,-1):
                GPIO.output(dac,decimal2binary(i))
                sleep(t)
finally:
    GPIO.output(dac,0)
    GPIO.cleanup()

        