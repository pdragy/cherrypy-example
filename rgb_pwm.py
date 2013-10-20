import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

pr = 18
pg = 23
pb = 24

GPIO.setup(18, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)

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
#p = GPIO.PWM(pr, 150)  # channel=12 frequency=50Hz
#p2 = GPIO.PWM(pg, 150)  # channel=12 frequency=50Hz
#p3 = GPIO.PWM(pb, 150)  # channel=12 frequency=50Hz
#led_pink(pr,pg,pb)
#p2.start(0)
#p3.start(0)
#while 1:
#	for dc in range(0, 101, 5):
#		p2.ChangeDutyCycle(dc)
#		p3.ChangeDutyCycle(dc)
#		time.sleep(0.05)
#	for dc in range(100, -1, -5):
#		p2.ChangeDutyCycle(dc)
#		p3.ChangeDutyCycle(dc)
#		time.sleep(0.05)
#
while(True):
	led_yellow(pr, pg, pb)
	time.sleep(0.05)
	#led_pink(pr, pg, pb)
	#time.sleep(0.05)
	#led_blue(pr, pg, pb)
	#time.sleep(0.05)
	#led_turquoise(pr, pg, pb)
	#time.sleep(0.05)
	#led_green(pr, pg, pb)
	#time.sleep(0.05)
	#led_yellow(pr, pg, pb)
	#time.sleep(0.05)

	

