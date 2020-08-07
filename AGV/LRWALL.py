from MovementFunctions import Hard_Right
from MovementFunctions import Hard_Left
from adafruit_motorkit import MotorKit
kit = MotorKit()

def LR_Wall(Right_Ultra_Distance, Left_Ultra_Distance):
    
    if Right_Ultra_Distance < 15:
        
        print('Too close Right Side!!!')
        
        Hard_Left()
        
    if Left_Ultra_Distance < 15:
        
        print('Too close Left Side!!!')
        
        Hard_Right()