import time
import wiringpi

def running_light(led_pins):
    # Move through the LED pins in sequence from left to right
    for i in range(len(led_pins)):
        # Turn on the LED (Set the corresponding input HIGH)
        wiringpi.digitalWrite(led_pins[i], 1)
        time.sleep(0.1)  # Wait for 0.1 seconds

        # Turn off the LED (Set the corresponding input LOW)
        wiringpi.digitalWrite(led_pins[i], 0)

# SETUP
print("Start Running Light Effect")

led_pins = [0, 1, 2, 3]  # GPIO pins for LEDs (WiringPi w0, w1, w2, w3)
wiringpi.wiringPiSetup()

# Set each pin to OUTPUT mode
for pin in led_pins:
    wiringpi.pinMode(pin, 1)

# MAIN - Infinite loop for continuous running light effect
while True:
    running_light(led_pins)
