import time
import RPi.GPIO as GPIO
    
#def Right_Ultra():
    
GPIO.setmode(GPIO.BOARD)

TRIG = 13
ECHO = 15

GPIO.setup(TRIG, GPIO.OUT)
GPIO.output(TRIG, 0)
GPIO.setup(ECHO, GPIO.IN)

time.sleep(0.2)
    
#print ("Measuring")


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

RD = (measure * 17000)
        
#print('U2')    
print(round(RD, 1))
    
time.sleep(.5)

GPIO.cleanup()



