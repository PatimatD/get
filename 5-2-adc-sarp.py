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
    l =[128, 64, 32, 16, 8, 4, 2, 1]
    q = 0
    for x in l:
        gpio.output(dac, decimal2binary(q+x))
        time.sleep(0.01)
        compValue = gpio.input(comp)
        if compValue == 1:
            q = q + x
        else: q = q
    gpio.output(dac, decimal2binary(q))
    voltage = (q / 256) * 3.3
    print(voltage)

try:
    while True:
        adc()
       
finally:
    gpio.output(dac, gpio.LOW)
    gpio.cleanup()
