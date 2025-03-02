import time
import wiringpi

def sos_signal(pin):
    # SOS pattern: ... --- ... (short, short, short, long, long, long, short, short, short)
    
    # Short pulse (0.5 seconds) for "S"
    for _ in range(3):  # Three short pulses for "S"
        wiringpi.digitalWrite(pin, 1)  # Turn on LED
        time.sleep(0.5)  # Wait for 0.5 seconds
        wiringpi.digitalWrite(pin, 0)  # Turn off LED
        time.sleep(0.5)  # Wait for 0.5 seconds
    
    # Long pulse (1.5 seconds) for "O"
    for _ in range(3):  # Three long pulses for "O"
        wiringpi.digitalWrite(pin, 1)  # Turn on LED
        time.sleep(1.5)  # Wait for 1.5 seconds
        wiringpi.digitalWrite(pin, 0)  # Turn off LED
        time.sleep(0.5)  # Wait for 0.5 seconds between long pulses

    # Short pulse (0.5 seconds) for "S"
    for _ in range(3):  # Three short pulses for "S"
        wiringpi.digitalWrite(pin, 1)  # Turn on LED
        time.sleep(0.5)  # Wait for 0.5 seconds
        wiringpi.digitalWrite(pin, 0)  # Turn off LED
        time.sleep(0.5)  # Wait for 0.5 seconds

# SETUP
print("Start SOS Signal")

gpio_pin = 1  # GPIO1 (WiringPi w1)

wiringpi.wiringPiSetup()

# Set GPIO1 as OUTPUT mode
wiringpi.pinMode(gpio_pin, 1)

# MAIN - Infinite loop for continuous SOS signal
while True:
    sos_signal(gpio_pin)
