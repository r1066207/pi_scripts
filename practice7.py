import wiringpi as wp
import time

# set pin numbers
LED_PIN = 2  # GPIO pin number connected to LED (WiringPi pin w2)

# initialize WiringPi
wp.wiringPiSetup()  # Initializes the WiringPi library for use

# set up LED pin as output
wp.pinMode(LED_PIN, wp.OUTPUT)  # Configures GPIO pin 2 (w2) as an OUTPUT pin

# blinking function
def blink(pin, numberBlinks, period, dutyCycle):
    timeHigh = period * dutyCycle / 100  # Duration of the HIGH state (LED ON)
    timeLow = period - timeHigh  # Duration of the LOW state (LED OFF)
    
    # Loop to blink LED the specified number of times
    for i in range(numberBlinks):
        wp.digitalWrite(pin, wp.HIGH)  # Turn LED ON (set pin HIGH)
        time.sleep(timeHigh)  # Wait for the duration of the HIGH state
        wp.digitalWrite(pin, wp.LOW)  # Turn LED OFF (set pin LOW)
        time.sleep(timeLow)  # Wait for the duration of the LOW state

# blink LED 20 times with a period of 0.5 seconds and a duty cycle of 75%
blink(LED_PIN, 20, 0.5, 75)

# cleanup
print("program executed")  # Output message indicating the program ran successfully
