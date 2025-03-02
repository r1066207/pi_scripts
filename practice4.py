import time
import wiringpi

def running_light(led_pins):
    # Move from left to right
    for i in range(len(led_pins)):
        wiringpi.digitalWrite(led_pins[i], 1)  # Turn on LED
        time.sleep(0.1)
        wiringpi.digitalWrite(led_pins[i], 0)  # Turn off LED

    # Move from right to left
    for i in range(len(led_pins) - 2, 0, -1):  # Skip first & last LED to avoid double blinking
        wiringpi.digitalWrite(led_pins[i], 1)  # Turn on LED
        time.sleep(0.1)
        wiringpi.digitalWrite(led_pins[i], 0)  # Turn off LED

# SETUP
print("Start Bi-Directional Running Light")

led_pins = [0, 1, 2, 3]  # GPIO pins for LEDs (WiringPi w0, w1, w2, w3)
wiringpi.wiringPiSetup()

# Set each pin to OUTPUT mode
for pin in led_pins:
    wiringpi.pinMode(pin, 1)

# MAIN - Infinite loop for continuous running light effect
while True:
    running_light(led_pins)
