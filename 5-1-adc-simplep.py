import RPi.GPIO as gpio
import time

dac = [26, 19, 13, 6, 5, 11, 9, 10] 
gpio.setmode(gpio.BCM)

comp = 4 
troyka = 17
gpio.setup(dac, gpio.OUT)
gpio.setup(comp, gpio.IN)
gpio.setup(troyka, gpio.OUT, initial = gpio.HIGH)

def decimal2binary(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

def adc():
    for x in range(256):
        gpio.output(dac, decimal2binary(x))
        time.sleep(0.01)
        compValue = gpio.input(comp)
        if compValue == 0:
            voltage = (x / 256) * 3.3
            print(voltage, decimal2binary(x))
            break


try:
    while True:
        adc()
       
finally:
    gpio.output(dac, gpio.LOW)
    gpio.cleanup()
