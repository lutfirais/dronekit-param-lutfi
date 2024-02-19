from __future__ import print_function
from dronekit import connect,VehicleMode,LocationGlobalRelative
import time

#Set up option parsing to get connection string
import argparse  
parser = argparse.ArgumentParser(description='Example showing how to set and clear vehicle channel-override information.')
parser.add_argument('--connect', 
                   help="vehicle connection target string. If not specified, SITL automatically started and used.")
args = parser.parse_args()
connection_string = args.connect

# Connect to the Vehicle
print('Connecting to vehicle on: %s' % connection_string)
# vehicle = connect(connection_string, wait_ready=True)
vehicle = connect('/dev/ttyAMA0',baud=57600,wait_ready = True)

# Listening to SERVO_OUTPUT_RAW mavlink topic
@vehicle.on_message('*') 
def listener(vehicle, name, m):
    # print(f"{m.servo1_raw}\t{m.servo2_raw}\t{m.servo3_raw}\t{m.servo4_raw}") # The Four PWM of the Quadcopter
    print(m)

'''
The above example worked, now try
    - Check Mavlink Message on actual Hardware
    - Check Current & RPM Value through mavlink on real Drone 
    - Check PWM Value if it's correct on real drone
    - Integrate with the previous code
'''

while True:
    continue