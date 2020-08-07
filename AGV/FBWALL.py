from MovementFunctions import Forward
from MovementFunctions import Backward
from adafruit_motorkit import MotorKit
import time

kit = MotorKit()


def FB_Wall(Front_Ultra_Distance, Back_Ultra_Distance): #Change name to something better
    if Front_Ultra_Distance < 10:
        
        print ('Backward')
        
        Backward()
        
        time.sleep(1.5)
        
    if Back_Ultra_Distance < 10:
        
        print ('Forward')
        
        Forward()
        
        
        