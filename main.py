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
#motor_a = Motor(Port.A)
motor_b = Motor(Port.B)
motor_c = Motor(Port.C)

# Go forward for 3 seconds
motor_b.run_time(500, 3000, Stop.BRAKE, False)
motor_c.run_time(500, 3000, Stop.BRAKE, True)

# Beep to end
ev3.speaker.beep(frequency=800, duration=500)