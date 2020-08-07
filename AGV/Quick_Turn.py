#from MovementFunctions import Turn_Left
#from MovementFunctions import Turn_Right
from adafruit_motorkit import MotorKit
kit = MotorKit()


def Quick_Turn(Right_Ultra_Distance, Left_Ultra_Distance, Front_Ultra_Distance, Back_Ultra_Distance):
    if (Left_Ultra_Distance + Front_Ultra_Distance) < Right_Ultra_Distance:
        print('Quick Right Turn')
        #return Turn_Left
    
        kit.motor1.throttle = 0.2
        kit.motor2.throttle = 1.0
        kit.motor3.throttle = 0.2
        kit.motor4.throttle = 1.0
        
    if (Right_Ultra_Distance + Front_Ultra_Distance) < Left_Ultra_Distance:
        
        print('Quick Left Turn')
        
        #return Turn_Right
        
        kit.motor1.throttle = 1.0
        kit.motor2.throttle = 0.2
        kit.motor3.throttle = 1.0
        kit.motor4.throttle = 0.2
        