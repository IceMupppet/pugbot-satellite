import RPi.GPIO as GPIO
import time, sys, termios, tty

GPIO.cleanup()

GPIO.setmode(GPIO.BCM) # Pins referenced by Broadcoms GPIO numbers, not the pin number of the RPi header

# Set labels and map them to GPIO numbers
ENA = 23
MA1 = 4
MA2 = 18
ENB = 17
MB1 = 22
MB2 = 27

# Set all used GPIOs to outputs
GPIO.setup(ENA, GPIO.OUT)
GPIO.setup(MA1, GPIO.OUT)
GPIO.setup(MA2, GPIO.OUT)
GPIO.setup(ENB, GPIO.OUT)
GPIO.setup(MB1, GPIO.OUT)
GPIO.setup(MB2, GPIO.OUT)

 
def bot_reverse():
        GPIO.output(ENA, True)
        GPIO.output(MA1, True)
        GPIO.output(MA2, False)
        GPIO.output(ENB, True)
        GPIO.output(MB1, True)
        GPIO.output(MB2, False)
	print "Driving BACK"

def bot_forward():
        GPIO.output(ENA, True)
        GPIO.output(MA1, False)
        GPIO.output(MA2, True)
        GPIO.output(ENB, True)
        GPIO.output(MB1, False)
        GPIO.output(MB2, True)
	print "Driving FORWARD"

def bot_left():
        GPIO.output(ENA, True)
        GPIO.output(MA1, True)
        GPIO.output(MA2, False)
        GPIO.output(ENB, True)
        GPIO.output(MB1, False)
        GPIO.output(MB2, True)
	print "Turning LEFT"

def bot_right():
        GPIO.output(ENA, True)
        GPIO.output(MA1, False)
        GPIO.output(MA2, True)
        GPIO.output(ENB, True)
        GPIO.output(MB1, True)
        GPIO.output(MB2, False)
	print "Turning RIGHT"

def bot_stop():
	GPIO.output(ENA, False)
	GPIO.output(MA1, False)
	GPIO.output(MA2, False)
	GPIO.output(ENB, False)
	GPIO.output(MB1, False)
	GPIO.output(MB2, False)
	print "STOP/RESET"


bot_stop()

print sys.argv[1]

if sys.argv[1] == "START":
        bot_stop()
elif sys.argv[1] == "UP":
        bot_forward()
elif sys.argv[1] == "DOWN":
        bot_reverse()
elif sys.argv[1] == "LEFT":
        bot_left()
elif sys.argv[1] == "RIGHT":
        bot_right()
elif sys.argv[1] == "STOP":
        bot_stop()


# Housekeeping
