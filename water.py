#!/usr/bin/env python

from time import sleep
import RPi.GPIO as GPIO
import os
 
GPIO.setmode(GPIO.BCM) 
INPUT_PIN = 4 
GPIO.setup(INPUT_PIN, GPIO.IN) 
is_low = False
# Create a function to run when the input is high
def inputLow(channel):
    is_low = True
    print 'low'

def inputHigh(channel):
    is_low = False
    print('high')

# Wait for the input to go low, run the function when it does
GPIO.add_event_detect(INPUT_PIN, GPIO.FALLING, callback=inputLow, bouncetime=200)

# Start a loop that never ends
while True:
    if GPIO.input(INPUT_PIN):
        print "stay low"
        os.system('echo "#00FF00" > indicator_light')
    else:
        print "stay high"
        os.system('echo "#FF0000" > indicator_light')
    sleep(1)
