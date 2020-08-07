import RPi.GPIO as GPIO
import time

def Front_Ultra():

    GPIO.setmode(GPIO.BCM)

    TRIG = 26
    ECHO = 16
    
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
        
    return(round(distance, 0))
        

GPIO.cleanup()