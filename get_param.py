from dronekit import connect, VehicleMode
import time
import argparse  
from pathlib import Path

# Making .txt log file
# file_name = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()) 
# Path(f'./Log/{file_name}.txt').touch()
# f = open(f"./Log/{file_name}.txt","a")

vehicle = connect('127.0.0.1:14550',wait_ready=True)
# SITL 127.0.0.1:14550
# Raspberry Pi -> Pixhawk /dev/ttyAMA0 baud =57600

last_attitude_cache = None
t = time.time()

# Print Header
local_time = time.localtime()
incTime = 0
# f.write(f"deltaTime(s) \t Time(s) \t Roll(rad) \t Pitch(rad) \t Yaw(rad) \t RollSpeed(rad/s) \t PitchSpeed(rad/s) \t YawSpeed(rad/s) \n")
# For debugging purposes
print(f"deltaTime(s)\tTime(s)\tRoll(rad)\tPitch(rad)\tYaw(rad)\tRollSpeed(rad/s)\tPitchSpeed(rad/s\tYawSpeed(rad/s)\tMotor1(PWM)\tMotor2(PWM)\tMotor3(PWM)\tMotor4(PWM)\t\n")

# Listening to SERVO_OUTPUT_RAW mavlink topic
@vehicle.on_message('SERVO_OUTPUT_RAW') 
def listener(vehicle, name, m):
    # print(f"{m.servo1_raw}\t{m.servo2_raw}\t{m.servo3_raw}\t{m.servo4_raw}") # The Four PWM of the Quadcopter
    global t
    global incTime
    
    deltaTime = time.time() - t
    t = time.time()
    incTime += deltaTime

    input_string = str(vehicle.attitude)

    # Split the string based on commas
    split_values = input_string.split(',')

    # Extract pitch, yaw, and roll values
    pitch = float(split_values[0].split('=')[1])
    yaw = float(split_values[1].split('=')[1])
    roll = float(split_values[2].split('=')[1])

    print(f"%.8f \t%.8f\t%.8f\t%.8f\t%.8f\t%.8f\t%.8f\t%.8f\t%d\t%d\t%d\t%d\n" %(deltaTime,incTime,roll,pitch,yaw,vehicle._rollspeed,vehicle._pitchspeed,vehicle._yawspeed,m.servo1_raw,m.servo2_raw,m.servo3_raw,m.servo4_raw))

# Adding Callback
# vehicle.add_attribute_listener('attitude', attitude_callback)
while True:
    continue