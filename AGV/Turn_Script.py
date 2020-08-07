from MovementFunctions import Turn_Right
from MovementFunctions import Turn_Left
from adafruit_motorkit import MotorKit

kit = MotorKit()

def Turn_Script(Right_Ultra_Distance, Left_Ultra_Distance):
    
    if Right_Ultra_Distance > 320:
        
        print('Turning Right')
        
        Turn_Right()
        
    if Left_Ultra_Distance > 320:
        
        print('Turning Left')
        
        Turn_Left()
        
        