#!/usr/bin/python3
"""
Python Practical Template
Keegan Crankshaw
Readjust this Docstring as follows:
Names: Kerry-Ann Couperthhwaite
Student Number: CPRKER002
Prac: 1
Date: <dd/mm/yyyy>
"""

# import Relevant Librares
import RPi.GPIO as GPIO
import time
import itertools
GPIO.setmode(GPIO.BCM)


#GPIO.setup() 3 leds putput
channelout_list = [17,27,22]
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
increaseBTN = 5
decreaseBTN = 6 
GPIO.setup(increaseBTN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(decreaseBTN, GPIO.IN, pull_up_down=GPIO.PUD_UP)


#Interrupts and Debouncing
GPIO.add_event_detect(5, GPIO.FALLING, callback=increase,
bouncetime=300)
GPIO.add_event_detect(6, GPIO.FALLING, callback=callback_method(),
bouncetime=300)
binaries = list(itertools.product([0,1], repeat=3))
counter = 0

def increase():
	global counter
	counter +=1
	if counter == 8:
		counter =0
	GPIO.output(channelout_list, binaries[counter])
	time.sleep(0.5)
def decrease():
	global counter
	counter -=1
	if counter == 8:
		counter=0
	GPIO.output(channelout_list, binaries[counter])

# Logic that you write
def main():
    pass
    print("write your logic here")


# Only run the functions if 
if __name__ == "__main__":
    # Make sure the GPIO is stopped correctly
    try:
        while True:
            main()
    except KeyboardInterrupt:
        print("Exiting gracefully")
        # Turn off your GPIOs here
        GPIO.cleanup()
    except Exception as e:
        GPIO.cleanup()
        print("Some other error occurred")
        print(e.message)
