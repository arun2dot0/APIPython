#!/usr/bin/python
import requests
import json

#ppopostConditions(22,55,253,500)

def postConditions(temp_celcius,humidity,light_intensity,sound_intensity):
    try:
        sound = sound_intensity/10
        fh = temp_celcius * 9/5 + 32
        data={
            "temperature": fh,
            "humidity": humidity,
            "lightintensity": light_intensity,
            "soundIntensity": sound
            }
        data_json = json.dumps(data)
        headers = { 'Accept' : 'application/json', 'Content-Type' : 'application/json'}

        response = requests.post('http://104.198.174.99:8080/metrics', data=data_json , headers=headers)

        print response.status_code
        print response.text

        #temperature in celcius
        #humidity in percent
        #light in illuminance
        #sound reading in decibels
    except IOError:   # Turn LED off before stopping
        print 'Unable to post data to cloud'
    return;

