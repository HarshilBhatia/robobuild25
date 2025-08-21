#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()


# Write your program here.
ev3.speaker.beep()

# Try a motor:
motor_lift = Motor(Port.A)
motor_left = Motor(Port.B)
motor_right = Motor(Port.C)
# color_sensor = ColorSensor(Port.S3)

# first straight 
motor_left.run_time(2000, 2500, Stop.BRAKE, False)
motor_right.run_time(2000, 2500, Stop.BRAKE, True)

# left turn 
motor_right.run_angle(500, 270, Stop.BRAKE, True)

wait(100)

# lift up 
motor_lift.run_angle(1000, 100, Stop.HOLD, True) # up


# back a little 
motor_left.run_time(-800, 500, Stop.BRAKE, False)
motor_right.run_time(-800, 500, Stop.BRAKE, True)

wait(100)

# smash
motor_lift.run_angle(1000, -120, Stop.HOLD, True) # down 
motor_lift.run_angle(1000, 100, Stop.HOLD, True) # up 

wait(100)

motor_left.run_time(-1000, 500, Stop.BRAKE, False)
motor_right.run_time(-1000, 500, Stop.BRAKE, True)

wait(2000)

motor_left.run_time(-1000, 500, Stop.BRAKE, False)
motor_right.run_time(-1000, 500, Stop.BRAKE, True)

wait(100)

# motor_left.run_until_stalled(200, Stop.COAST, False)
# motor_right.run_until_stalled(200, Stop.COAST, True)

# reset angle
# curr_angle = motor_lift.angle()
# print(curr_angle)
# # if (curr_angle != 0):

# motor_lift.run_angle(50, -70, Stop.HOLD, True)
# curr_angle = motor_lift.angle()
# print(curr_angle)
# # motor level -8?? 

# motor_left.run_angle(500, 90, Stop.BRAKE, True)
# # motor_right.run_angle(500, -45, Stop.BRAKE, True)
# wait(100)
# motor_left.run_time(300, 1500, Stop.BRAKE, False)
# motor_right.run_time(300, 1500, Stop.BRAKE, True)

# wait(100)

# #motor_left.run_angle(500, -30, Stop.BRAKE, False)
# motor_right.run_angle(500, 90, Stop.BRAKE, True)

# motor_left.run_time(300, 5000, Stop.BRAKE, False)
# motor_right.run_time(300, 5000, Stop.BRAKE, True)

# motor_left.run_time(-500, 1500, Stop.BRAKE, False)
# motor_right.run_time(-500, 1500, Stop.BRAKE, True)

# motor_left.run_angle(500, -180, Stop.BRAKE, False)
# motor_right.run_angle(500, 180, Stop.BRAKE, True)

# motor_left.run_time(200, 2000, Stop.BRAKE, False)
# motor_right.run_time(200, 2000, Stop.BRAKE, True)

# # coral forward task 
# motor_left.run_time(200, 2000, Stop.BRAKE, False)
# motor_right.run_time(200, 2000, Stop.BRAKE, True)

# motor_left.run_time(-200, 2000, Stop.BRAKE, False)
# motor_right.run_time(-200, 2000, Stop.BRAKE, True)

# # Go forward for 3 seconds
# motor_left.run_time(500, 3000, Stop.BRAKE, False)
# motor_right.run_time(500, 3000, Stop.BRAKE, True)

# motor_b.run_time(-500, 3000, Stop.BRAKE, False)
# motor_c.run_time(500, 3000, Stop.BRAKE, True)

# # left turn
# motor_left.run_angle(500, -180, Stop.BRAKE, False)
# motor_right.run_angle(500, 180, Stop.BRAKE, True)

# # right turn
# motor_left.run_angle(500, 180, Stop.BRAKE, False)
# motor_right.run_angle(500, -180, Stop.BRAKE, True)

# # trying lift 

#motor_lift.run_angle(50, -180, Stop.HOLD, True)
# wait(1000)
#motor_lift.run_angle(50, 360, Stop.HOLD, True)


# wait(1000)
# motor_lift.run_angle(500, -180, Stop.BRAKE, True)
# print(motor_lift.angle())
# print("motor position", motor_lift.position())

# 
# print("color", color_sensor.)
# print("pressed?", touch_sensor.pressed())

# Beep to end
ev3.speaker.beep(frequency=800, duration=500)