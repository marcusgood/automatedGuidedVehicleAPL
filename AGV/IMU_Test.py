from sense_hat import SenseHat

sense = SenseHat()

sense.set_imu_config(True, True, True)

orientation_rad = sense.get_orientation_radians()

print('p: {pitch}, r: {roll}, y: {yaw}'.format(**orientation_rad))

