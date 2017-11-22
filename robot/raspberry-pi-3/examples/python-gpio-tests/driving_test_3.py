import RPi.GPIO as GPIO
import time, sys, termios, tty

GPIO.setmode(GPIO.BCM) # Pins referenced by Broadcoms GPIO numbers, not the pin number of the RPi header

# Set labels and map them to GPIO numbers
ENA = 14
MA1 = 15
MA2 = 18
ENB = 17
MB1 = 27
MB2 = 22

# Set all used GPIOs to outputs
GPIO.setup(ENA, GPIO.OUT)
GPIO.setup(MA1, GPIO.OUT)
GPIO.setup(MA2, GPIO.OUT)
GPIO.setup(ENB, GPIO.OUT)
GPIO.setup(MB1, GPIO.OUT)
GPIO.setup(MB2, GPIO.OUT)

ENAPWM = GPIO.PWM(ENA, 100)
ENBPWM = GPIO.PWM(ENB, 100)

# Set defualts
ENAPWM.stop()
GPIO.output(MA1, False)
GPIO.output(MA2, False)
ENBPWM.stop()
GPIO.output(MB1, False)
GPIO.output(MB2, False)

#time.sleep(0.5)


# The getch method can determine which key has been pressed
# by the user on the keyboard by accessing the system files
# It will then return the pressed key as a variable
def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


def bot_forward():
        ENAPWM.start(100)
        GPIO.output(MA1, True)
        GPIO.output(MA2, False)
        ENBPWM.start(100)
        GPIO.output(MB1, True)
        GPIO.output(MB2, False)

def bot_reverse():
        ENAPWM.start(100)
        GPIO.output(MA1, False)
        GPIO.output(MA2, True)
        ENBPWM.start(100)
        GPIO.output(MB1, False)
        GPIO.output(MB2, True)

def bot_left():
        ENAPWM.start(75)
        GPIO.output(MA1, True)
        GPIO.output(MA2, False)
        ENBPWM.start(75)
        GPIO.output(MB1, False)
        GPIO.output(MB2, True)

def bot_right():
        ENAPWM.start(75)
        GPIO.output(MA1, False)
        GPIO.output(MA2, True)
        ENBPWM.start(75)
        GPIO.output(MB1, True)
        GPIO.output(MB2, False)

def bot_stop():
	ENAPWM.stop()
	GPIO.output(MA1, False)
	GPIO.output(MA2, False)
	ENBPWM.stop()
	GPIO.output(MB1, False)
	GPIO.output(MB2, False)

# Instructions for when the user has an interface
print("w/s: acceleration")
print("a/d: steering")
print("x: exit")

# Infinite loop that will not end until the user presses the
# exit key
while True:
	# Keyboard character retrieval method is called and saved
	# into variable
	char = getch()

	# The car will drive forward when the "w" key is pressed
	if(char == "w"):
		bot_forward()

	# The car will reverse when the "s" key is pressed
	if(char == "s"):
		bot_reverse()

	# The "a" key will toggle the steering left
	if(char == "a"):
        	bot_left()

	# The "d" key will toggle the steering right
	if(char == "d"):
		bot_right()

	# The "e" key will stop the robot
	if(char == "e"):
		bot_stop()

	# The "x" key will break the loop and exit the program
	if(char == "x"):
		print("Program Ended")
		break

	# At the end of each loop the acceleration motor will stop
	# and wait for its next command
	#bot_disable_motors()

	# The keyboard character variable will be set to blank, ready
	# to save the next key that is pressed
	char = ""


bot_stop()

# Housekeeping
GPIO.cleanup()
