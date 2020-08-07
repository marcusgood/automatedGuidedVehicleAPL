from adafruit_Motorkit import Motorkit
kit = Motorkit()

def Motor_Family():  #Class this? and the ULTRA FAM??
    back_left_motor = kit.motor1.throttle
    back_right_motor = kit.motor2.throttle
    front_left_motor = kit.motor3.throttle
    front_right_motor = kit.motor4.throttle
