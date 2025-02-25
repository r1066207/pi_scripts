import time
import wiringpi
import sys

def blink(led_pins):
    # Turn all LEDs on (by setting pins LOW)
    for pin in led_pins:
        wiringpi.digitalWrite(pin, 0)   # Set pin LOW (LED on)
    time.sleep(0.1)  # Wait for 0.1 seconds

    # Turn all LEDs off (by setting pins HIGH)
    for pin in led_pins:
        wiringpi.digitalWrite(pin, 1)   # Set pin HIGH (LED off)
    time.sleep(0.1)  # Wait for 0.1 seconds

# SETUP
print("Start")
led_pins = [0, 1, 2, 3]  # GPIO pins for LEDs (WiringPi w0, w1, w2, w3)
wiringpi.wiringPiSetup()

# Set each pin to OUTPUT mode
for pin in led_pins:
    wiringpi.pinMode(pin, 1)

# MAIN - Infinite loop for continuous blinking
while True:
    blink(led_pins)

# cleanup
# No cleanup needed since the program runs infinitely
