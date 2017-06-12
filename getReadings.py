#!/usr/bin/python
import grovepi
import apiCall
from time import sleep
import math

# Connections
sound_sensor = 0        # port A0
light_sensor = 1        # port A1
temperature_sensor = 7  # port D2
#led = 3               cd  # port D3


while True:
	try:
                light_intensity = grovepi.analogRead(light_sensor)
                print(light_intensity)
                

                # Get sound level
                sound_level = grovepi.analogRead(sound_sensor)
                print(sound_level)
               
                # Get value from temperature sensor
                [t,h]=[0,0]
                [t,h] = grovepi.dht(temperature_sensor,0)
                print(t)
                print(h)
                apiCall.postConditions(t,h,light_intensity,sound_level)
                sleep(300)
	except IOError as ie:
                print("Error "+ie)
