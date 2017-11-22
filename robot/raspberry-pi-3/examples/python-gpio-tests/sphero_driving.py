import RPi.GPIO as GPIO
import serial
import time, sys, termios, tty


# Pins referenced by Broadcoms GPIO numbers, not the pin number of the RPi header
GPIO.setmode(GPIO.BCM)

# Set up the serial port
port = serial.Serial("/dev/ttyAMA0", baudrate=115200, timeout=3.0)

# Set global variables
currentHeading = 0
currentSpeed = 0

# Send a command to the Sphero PCB
def writeCommand(command):
	port.write(command)
	port.write("\r")

	while True:
		ch = port.read()
		print(ch)
		if ch=='>':
			return 1


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
	global currentSpeed
	writeCommand("l1")
	currentSpeed = 255
        writeCommand("roll %s %s" %(str(currentHeading), str(currentSpeed)))
	time.sleep(0.5)
	writeCommand("l0")

def bot_reverse():
	bot_stop()
        writeCommand("l0")
	writeCommand("mb 200")
	time.sleep(0.5)
	writeCommand("l1")

def bot_left():
	global currentHeading
	writeCommand("l1")
	if (currentHeading < 10):
		currentHeading = 360 + (currentHeading - 10) 
	else:
		currentHeading = currentHeading - 10
        writeCommand("roll %s %s" %(str(currentHeading), str(currentSpeed)))
	time.sleep(0.5)
	writeCommand("l0")

def bot_right():
	global currentHeading
	writeCommand("l1")
	if (currentHeading > 349):
		currentHeading = abs(359 - (currentHeading + 10))
	else:
		currentHeading = currentHeading + 10
	currentHeading = currentHeading + 10
        writeCommand("roll %s %s" %(str(currentHeading), str(currentSpeed)))
	time.sleep(0.5)
	writeCommand("l0")

def bot_stop():
	global currentSpeed
        currentSpeed = 0
        writeCommand("roll %s %s" %(str(currentHeading), str(currentSpeed)))


# Clear the F8 in the serial buffer
#writeCommand("")
#writeCommand("smu")
#writeCommand("sh 0")
#writeCommand("l1")

print("first debug statement")
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
		bot_stop()
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
