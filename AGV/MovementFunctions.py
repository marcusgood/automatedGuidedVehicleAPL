#from ULTRAFAM import Ultra_Family #PROLLY SHOULD BE A CLASS
#from MOTORFAM import Motor_Family #PROLLY SHOULD BE A CLASS

from adafruit_motorkit import MotorKit
kit = MotorKit()


#kit.motor1.throttle is the back right motor (from the battery pack facing the viewer)
#kit.motor2.throttle is the back left motor
#kit.motor3.throttle is the front right motor
#kit.motor4.throttle is the fron left motor

def Forward():
    kit.motor1.throttle = 1
    kit.motor2.throttle = 1
    kit.motor3.throttle = 1
    kit.motor4.throttle = 1
    
def Backward():
    kit.motor1.throttle = -0.8
    kit.motor2.throttle = -0.8
    kit.motor3.throttle = -0.8
    kit.motor4.throttle = -0.8
        
def Slight_Right():
    kit.motor1.throttle = 0.4
    kit.motor2.throttle = 0.8
    kit.motor3.throttle = 0.4
    kit.motor4.throttle = 0.8

def Slight_Left():
    kit.motor1.throttle = 0.8
    kit.motor2.throttle = 0.4
    kit.motor3.throttle = 0.8
    kit.motor4.throttle = 0.4
    
def Turn_Left():
    kit.motor1.throttle = 1.0
    kit.motor2.throttle = 0.2
    kit.motor3.throttle = 1.0
    kit.motor4.throttle = 0.2
    
def Turn_Right():
    kit.motor1.throttle = 0.2
    kit.motor2.throttle = 1.0
    kit.motor3.throttle = 0.2
    kit.motor4.throttle = 1.0
    
def Hard_Right():
    kit.motor1.throttle = 0.3
    kit.motor2.throttle = 1.0
    kit.motor3.throttle = 0.3
    kit.motor4.throttle = 1.0
    
def Hard_Left():
    kit.motor1.throttle = 1.0
    kit.motor2.throttle = 0.3
    kit.motor3.throttle = 1.0
    kit.motor4.throttle = 0.3
    
    
    
    
    
    
    
    
    
    
    
    
    
    