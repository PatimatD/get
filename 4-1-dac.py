import RPi.GPIO as GPIO
import sys
def decimal2binary(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]


dac=[26,19,13,6,5,11,9,10]

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
try:
    while('True'):
        a=input('input 0-255  ')
        if a == 'q':
            sys.exit()
        elif a.isdigit() and 0<=int(a)<=255:
            GPIO.output(dac,decimal2binary(int(a)))
            print("{:.4f}".format(int(a)/256*3.3))
        if a.isdigit() and 0<=int(a)>255:
            print('number must be <255')
        elif not a.isdigit():
            if a[0]=='-':
                print('number must be>0')
            else: 
                for i in range(len(a)):
                    k=0
                    if a[i]=='.' or a[i]==',':
                        k=1
                        print('number must be integer')
                        break
                if k==0:
                    print('it is str')
            print('input number')     
finally:
    GPIO.output(dac,0)
    GPIO.cleanup()
