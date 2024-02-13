from dronekit import connect, VehicleMode
import time
import argparse  

vehicle = connect('127.0.0.1:14550',wait_ready=True)
last_attitude_cache = None
t = time.time()

# Print Header
local_time = time.localtime()
incTime = 0
print("Current Time : ",time.strftime("%Y-%m-%d %H:%M:%S",local_time))
print(f"deltaTime(s) \t Time(s) \t Roll(rad) \t Pitch(rad) \t Yaw(rad) \t RollSpeed(rad/s) \t PitchSpeed(rad/s) \t YawSpeed(rad/s) ")

# Callback function that prints attitude info 
# Big thanks to ajayaru <3
def attitude_callback(self, attr_name, value):
    global last_attitude_cache
    global t
    global incTime
    input_string = str(value)

    # Split the string based on commas
    split_values = input_string.split(',')

    # Extract pitch, yaw, and roll values
    pitch = float(split_values[0].split('=')[1])
    yaw = float(split_values[1].split('=')[1])
    roll = float(split_values[2].split('=')[1])

    deltaTime = time.time() - t
    t = time.time()
    incTime += deltaTime
    print(f"{deltaTime} \t {incTime} \t {roll} \t {pitch} \t {yaw} \t {float(vehicle._rollspeed)} \t {float(vehicle._pitchspeed)} \t {float(vehicle._yawspeed)} \n")
    last_attitude_cache=value

# Adding Callback
vehicle.add_attribute_listener('attitude', attitude_callback)
while True:
    continue