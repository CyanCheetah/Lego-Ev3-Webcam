#!/usr/bin/env python3
from ev3dev2.sensor import INPUT_2
import os
from ev3dev2.motor import OUTPUT_B
import time
import ev3dev2.sensor as sensor
import ev3dev2.motor as motor
import ev3dev2.sound as sound
from ev3dev2.sound import Sound
from ev3dev2.sensor.lego import ColorSensor
color_sensor = ColorSensor(INPUT_2)
m = motor.LargeMotor(OUTPUT_B)
s = sound.Sound()
color_names = {
    1: 'Black',
    2: 'Blue',
    3: 'Green',
    4: 'Yellow',
    5: 'Red',
    6: 'White',
    7: 'Brown'
}
while True:

    color_value = color_sensor.color
    if color_value in color_names:
        m.on_for_rotations(-50, 0.25)
        s.speak(color_names[color_value])
        time.sleep(0.15)
        m.on_for_rotations(50, 0.25)
        

