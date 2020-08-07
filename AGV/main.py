from Center_Loop import Center_Loop
from ULTRA1 import Left_Ultra
from ULTRA2 import Right_Ultra
from ULTRA3 import Front_Ultra
from ULTRA4 import Back_Ultra
from FBWALL import FB_Wall
from Turn_Script import Turn_Script
from LRWALL import LR_Wall
  
while True:
    Right_Ultra_Distance = Right_Ultra()
    Left_Ultra_Distance = Left_Ultra()
    Front_Ultra_Distance = Front_Ultra()
    Back_Ultra_Distance = Back_Ultra()


    Center_Loop(Right_Ultra_Distance, Left_Ultra_Distance)
       
    FB_Wall(Front_Ultra_Distance, Back_Ultra_Distance)
    
    Turn_Script(Right_Ultra_Distance, Left_Ultra_Distance)
    
    LR_Wall(Right_Ultra_Distance, Left_Ultra_Distance)
    
    
    
    
