import time
import wiringpi
import sys

def blink(_pin):
    wiringpi.digitalWrite(_pin, 1)   # Write 1 (HIGH) to pin
    time.sleep(0.5)                
    wiringpi.digitalWrite(_pin, 0)   # Write 0 (HIGH) to pin
    time.sleep(0.5)

#SETUP
print("Start")
pin = 2
wiringpi.wiringPiSetup()
wiringpi.pinMode(pin, 1)   # set pin to mode 1 (OUTPUT)

#MAIN (infinite loop for continuous blinking)
while True:
    blink(pin)

#cleanup (no cleanup needed, because the program will run indefinitely)