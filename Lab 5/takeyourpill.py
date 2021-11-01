import time
import digitalio
import board
import busio
from adafruit_servokit import ServoKit


# Configuration for CS and DC pins (these are FeatherWing defaults on M0/M4):
cs_pin = digitalio.DigitalInOut(board.CE0)
dc_pin = digitalio.DigitalInOut(board.D25)
reset_pin = None

# Config for display baudrate (default max is 24mhz):
BAUDRATE = 64000000

# Setup SPI bus using hardware SPI:
spi = board.SPI()

#initialize Buttons
buttonA = digitalio.DigitalInOut(board.D23)
buttonB = digitalio.DigitalInOut(board.D24)
buttonA.switch_to_input()
buttonB.switch_to_input()


# Set channels to the number of servo channels on your kit.
# There are 16 channels on the PCA9685 chip.
kit = ServoKit(channels=16)

# Name and set up the servo according to the channel you are using.
servo = kit.servo[0]

# Set the pulse width range of your servo for PWM control of rotating 0-180 degree (min_pulse, max_pulse)
# Each servo might be different, you can normally find this information in the servo datasheet
#If the servo didn't sweep the full expected range, then try adjusting the minimum and maximum pulse widths 
#using set_pulse_width_range(min_pulse, max_pulse).
servo.set_pulse_width_range(500, 2500)


# You can change the total angle by setting actuation_range.
# servo.servo[0].actuation_range = 160
# servo.actuation_range = 160


while True:

    if buttonA.value and not buttonB.value:  # just button A pressed

            # Set the servo to 180 degree position
            servo.angle = 90
            time.sleep(2)
            servo.angle = 0
    else:
            # Set the servo to 0 degree position
            servo.angle = 180
            time.sleep(2)
        
    # except KeyboardInterrupt:
    #     # Once interrupted, set the servo back to 0 degree position
    #     servo.angle = 0
    time.sleep(1)
    break
