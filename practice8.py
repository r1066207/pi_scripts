import wiringpi as wp
import time

# Set pin numbers for LEDs (using software PWM)
LED_PINS = [0, 1, 2, 3]  # GPIO pins for your LEDs

# Initialize WiringPi
wp.wiringPiSetup()

# Set up each pin for software PWM output
for pin in LED_PINS:
    wp.pinMode(pin, wp.OUTPUT)  # Set pin mode to OUTPUT
    wp.softPwmCreate(pin, 0, 1023)  # Initialize software PWM (range: 0 to 1023)

# Fade LEDs in 4 steps: 25%, 50%, 75%, 100% brightness
brightness_levels = [256, 512, 768, 1023]  # 25%, 50%, 75%, 100% (PWM range 0-1023)

# Function to fade LEDs
def fade_leds(led_pins, brightness_levels, delay_time):
    for brightness in brightness_levels:
        for pin in led_pins:
            wp.softPwmWrite(pin, brightness)  # Set software PWM value for each LED
        time.sleep(delay_time)  # Wait for 2 seconds between steps

# Main program
try:
    while True:
        fade_leds(LED_PINS, brightness_levels, 2)  # Fade LEDs with 2s delay between steps
except KeyboardInterrupt:
    print("\nProgram interrupted. Exiting...")
finally:
    print("Program executed")
