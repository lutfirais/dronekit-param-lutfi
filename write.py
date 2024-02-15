from dronekit import connect, VehicleMode
import time
import argparse
import RPi.GPIO as GPIO
from pathlib import Path

#vehicle = connect('127.0.0.1:14550',wait_ready=True)
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(16, GPIO.OUT, initial=GPIO.LOW) #16
GPIO.output(16, GPIO.HIGH)

vehicle = connect('/dev/ttyAMA0',baud=57600,wait_ready = True)
# SITL 127.0.0.1:14550
# Raspberry Pi -> Pixhawk /dev/ttyAMA0 baud =57600

last_attitude_cache = None
t = time.time()

# Print Header
local_time = time.localtime()
incTime = 0

# Making .txt log file
file_name = time.strftime("%Y-%m-%d_%H:%M:%S",time.localtime()) 
Path(f'/home/drone/dronekit-param/Log/{file_name}.txt').touch()
f = open(f"/home/drone/dronekit-param/Log/{file_name}.txt","a")
f.write(f"deltaTime(s);Time(s);Roll(rad);Pitch(rad);Yaw(rad);RollSpeed(rad/s);PitchSpeed(rad/s);YawSpeed(rad/s) \n")

# Callback function that prints attitude info 
# Big thanks to ajayaru <3
def attitude_callback(self, attr_name, value):
    global last_attitude_cache
    global t
    global incTime
    input_string = str(value)
    GPIO.output(16, GPIO.LOW) 

    # Split the string based on commas
    split_values = input_string.split(',')

    # Extract pitch, yaw, and roll values
    pitch = float(split_values[0].split('=')[1])
    yaw = float(split_values[1].split('=')[1])
    roll = float(split_values[2].split('=')[1])

    deltaTime = time.time() - t
    t = time.time()
    incTime += deltaTime
    # print("paket received !")
    f.write(f"%.8f;%.8f;%.8f;%.8f;%.8f;%.8f;%.8f;%.8f \n" %(deltaTime,incTime,roll,pitch,yaw,vehicle._rollspeed,vehicle._pitchspeed,vehicle._yawspeed))
    last_attitude_cache=value

# Adding Callback
vehicle.add_attribute_listener('attitude', attitude_callback)
while True:
    continue
