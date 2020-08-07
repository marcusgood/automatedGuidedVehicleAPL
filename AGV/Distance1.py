import RPi.GPIO as GPIO
import time
    
GPIO.setmode(GPIO.BOARD)

TRIG = 23
ECHO = 24


GPIO.setup(TRIG, GPIO.OUT)
GPIO.output(TRIG, 0)

GPIO.setup(ECHO, GPIO.IN)

time.sleep(0.2)

print ("Measuring")

while True:

    GPIO.output(TRIG, 1)
    time.sleep(0.00001)
    GPIO.output(TRIG, 0)

    while GPIO.input(ECHO) ==0:
        pass
        start = time.time()

    while GPIO.input(ECHO) ==1:
        pass
        stop = time.time()

    measure = (stop - start)

    distance1 = (measure * 17000)
    
    if distance1 > 5:
        print("hello")

    print(distance1)
    
    time.sleep(0.5)

GPIO.cleanup()
