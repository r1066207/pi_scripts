import time
import wiringpi

def running_light(led_pins):
    # Turn on LED1 and LED3 together, then turn them off
    wiringpi.digitalWrite(led_pins[0], 1)  # LED1 ON
    wiringpi.digitalWrite(led_pins[2], 1)  # LED3 ON
    time.sleep(0.5)  # Wait for 0.5 seconds
    wiringpi.digitalWrite(led_pins[0], 0)  # LED1 OFF
    wiringpi.digitalWrite(led_pins[2], 0)  # LED3 OFF
    time.sleep(1)  # 1 second interval

    # Turn on LED2 and LED4 together, then turn them off
    wiringpi.digitalWrite(led_pins[1], 1)  # LED2 ON
    wiringpi.digitalWrite(led_pins[3], 1)  # LED4 ON
    time.sleep(0.5)  # Wait for 0.5 seconds
    wiringpi.digitalWrite(led_pins[1], 0)  # LED2 OFF
    wiringpi.digitalWrite(led_pins[3], 0)  # LED4 OFF
    time.sleep(1)  # 1 second interval

# SETUP
print("Start LED Pairs On-Off Effect")

led_pins = [0, 1, 2, 3]  # GPIO pins for LEDs (WiringPi w0, w1, w2, w3)
wiringpi.wiringPiSetup()

# Set each pin to OUTPUT mode
for pin in led_pins:
    wiringpi.pinMode(pin, 1)

# MAIN - Infinite loop for continuous LED pair on-off effect
while True:
    running_light(led_pins)
