import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

TRIG = 17
ECHO = 18
    
GPIO.setup(TRIG, GPIO.OUT)
GPIO.output(TRIG, 0)

GPIO.setup(ECHO, GPIO.IN)

time.sleep(0.2)


GPIO.output(TRIG, 1)
time.sleep(0.00001)
GPIO.output(TRIG, 0)

while GPIO.input(ECHO) ==0:
    pass
    start = time.time() #Time signal sent out

while GPIO.input(ECHO) ==1:
    pass
    stop = time.time() #Time signal received

measure = (stop - start) #Time signal took to go to and from object

distance = (measure * 17000) #Converts to centimeters
        
print(round(distance, 0))
        

GPIO.cleanup()