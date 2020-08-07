import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

TRIG1 = 7
ECHO1 = 12
TRIG2 = 11
ECHO2 = 13

GPIO.setup(TRIG1, GPIO.OUT)
GPIO.output(TRIG1, 0)

GPIO.setup(ECHO1, GPIO.IN)

time.sleep(0.1)

print ("Measuring")

GPIO.output(TRIG1, 1)
time.sleep(0.00001)
GPIO.output(TRIG1, 0)

while GPIO.input(ECHO1) ==0:
    pass
start = time.time()

while GPIO.input(ECHO1) ==1:
    pass
stop = time.time()

distance = (stop - start)

print(distance * 17000)

GPIO.cleanup()