from ULTRA1 import distance1
from ULTRA2 import distance2
from adafruit_motorkit import MotorKit
import time
from ULTRA1 import Ultra_Left

kit = MotorKit()
center = ((distance1 + distance2)/2)
back_left_motor = kit.motor1.throttle
back_right_motor = kit.motor2.throttle
front_left_motor = kit.motor3.throttle
front_right_motor = kit.motor4.throttle


while distance1 > 5 distance2 > 5:
    back_left_motor = 0.8
    back_right_motor = 0.8
    front_left_motor = 0.8
    front_right_motor = 0.8


elif distance1 > 200: #Turn Left Slower For Doorway
    back_left_motor = 0.4  #Left Turn Slower
    back_right_motor = 1.0
    front_left_motor = 0.4
    front_right_motor = 1.0

    
elif distance2 > 200: #Turn Right Slower For Doorway
    back_left_motor = 1.0  #Right Turn Slower
    back_right_motor = 0.4
    front_left_motor = 1.0
    front_right_motor = 0.4
    
    
    