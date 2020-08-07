from adafruit_motorkit import MotorKit
from MovementFunctions import Slight_Right
from MovementFunctions import Forward
from MovementFunctions import Slight_Left

kit = MotorKit()

def Center_Loop(Right_Ultra_Distance, Left_Ultra_Distance):
    
    if Right_Ultra_Distance < Left_Ultra_Distance:
        
        print('Left')
        
        Slight_Left()
    
    if Right_Ultra_Distance > Left_Ultra_Distance:
        
        print('Right')
        
        Slight_Right()
    
    if Right_Ultra_Distance == Left_Ultra_Distance:
        
        print('Forward')
        
        Forward()
        