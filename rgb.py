import RPi.GPIO as GPIO
import time
import subprocess
GPIO.setmode(GPIO.BCM)

pr = 18
pg = 23
pb = 24

GPIO.setup(pr, GPIO.OUT)
GPIO.setup(pg, GPIO.OUT)
GPIO.setup(pb, GPIO.OUT)

def led_off(r, g, b):
	GPIO.output(r, True)
	GPIO.output(g, True)
	GPIO.output(b, True)

def led_white(r, g, b):
	GPIO.output(r, False)
	GPIO.output(g, False)
	GPIO.output(b, False)

def led_red(r, g, b):
	GPIO.output(r, False)
	GPIO.output(g, True)
	GPIO.output(b, True)

def led_green(r, g, b):
	GPIO.output(r, True)
	GPIO.output(g, False)
	GPIO.output(b, True)

def led_blue(r, g, b):
	GPIO.output(r, True)
	GPIO.output(g, True)
	GPIO.output(b, False)

def led_yellow(r, g, b):
	GPIO.output(r, False)
	GPIO.output(g, False)
	GPIO.output(b, True)

def led_turquoise(r, g, b):
	GPIO.output(r, True)
	GPIO.output(g, False)
	GPIO.output(b, False)

def led_pink(r, g, b):
	GPIO.output(r, False)
	GPIO.output(g, True)
	GPIO.output(b, False)

def rainbow(r, g, b):
	led_red(pr, pg, pb)
	time.sleep(0.05)
	led_pink(pr, pg, pb)
	time.sleep(0.05)
	led_blue(pr, pg, pb)
	time.sleep(0.05)
	led_turquoise(pr, pg, pb)
	time.sleep(0.05)
	led_green(pr, pg, pb)
	time.sleep(0.05)
	led_yellow(pr, pg, pb)
	time.sleep(0.05)

while(True):
	color = subprocess.check_output(["tail", "-n", "1", "indicator_light"])

	
	r = ('FF' in color[1:3])
	g = ('FF' in color[3:5])
	b = ('FF' in color[5:7])
	if r: print "r"
	if g: print "g"
	if b: print "b"
	GPIO.output(pr, not r)
	GPIO.output(pg, not g)
	GPIO.output(pb, not b)
	time.sleep(5)
	
	
	
	

