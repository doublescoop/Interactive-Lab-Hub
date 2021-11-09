import time
import board
import digitalio
from omxplayer.player import OMXPlayer
import busio
from adafruit_servokit import ServoKit
# import qwiic_button
import tensorflow.keras
from PIL import Image, ImageOps
import numpy as np
import cv2
import sys


#initalize green button
# my_button = qwiic_button.QwiicButton()
file = 'redorblue.wav'



#initialize Buttons
buttonA = digitalio.DigitalInOut(board.D23)
buttonB = digitalio.DigitalInOut(board.D24)
buttonA.switch_to_input()
buttonB.switch_to_input()


# Configuration for CS and DC pins (these are FeatherWing defaults on M0/M4):
cs_pin = digitalio.DigitalInOut(board.CE0)
dc_pin = digitalio.DigitalInOut(board.D25)
reset_pin = None

# Config for display baudrate (default max is 24mhz):
BAUDRATE = 64000000

# Setup SPI bus using hardware SPI:
spi = board.SPI()

#========tensorflow==============
# Disable scientific notation for clarity
np.set_printoptions(suppress=True)

img = None
webCam = False
if(len(sys.argv)>1 and not sys.argv[-1]== "noWindow"):
   try:
      print("I'll try to read your image")
      img = cv2.imread(sys.argv[1])
      if img is None:
         print("Failed to load image file:", sys.argv[1])
   except:
      print("Failed to load the image are you sure that:", sys.argv[1],"is a path to an image?")
else:
   try:
      print("Trying to open the Webcam.")
      cap = cv2.VideoCapture(0)
      if cap is None or not cap.isOpened():
         raise("No camera")
      webCam = True
   except:
      print("Unable to access webcam.")


# Load the model
model = tensorflow.keras.models.load_model('keras_model.h5')
# Load Labels:
labels=[]
f = open("labels.txt", "r")
for line in f.readlines():
    if(len(line)<1):
        continue
    labels.append(line.split(' ')[1].strip())



#==============servo==============
# Set channels to the number of servo channels on your kit.
# There are 16 channels on the PCA9685 chip.
kit = ServoKit(channels=16)

# Name and set up the servo according to the channel you are using.
servo1 = kit.servo[0]
servo2 = kit.servo[15]


# Set the pulse width range of your servo for PWM control of rotating 0-180 degree (min_pulse, max_pulse)
# Each servo might be different, you can normally find this information in the servo datasheet
#If the servo didn't sweep the full expected range, then try adjusting the minimum and maximum pulse widths 
#using set_pulse_width_range(min_pulse, max_pulse).
servo1.set_pulse_width_range(500, 2500)
servo2.set_pulse_width_range(500, 2500)


# You can change the total angle by setting actuation_range.
# servo.servo[0].actuation_range = 160
# servo.actuation_range = 160

# my_button.LED_on(150)

while True: 
   # my_button.LED_on(150)
   
   # if my_button.is_button_pressed() == True:
      # OMXPlayer(file)
      # my_button.LED_off()

      # time.sleep(35)

      if webCam:
         ret, img = cap.read()

         rows, cols, channels = img.shape
         data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

         size = (224, 224)
         img =  cv2.resize(img, size, interpolation = cv2.INTER_AREA)
         #turn the image into a numpy array
         image_array = np.asarray(img)

         # Normalize the image
         normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
         # Load the image into the array
         data[0] = normalized_image_array

         # run the inference
         prediction = model.predict(data)
         print("I think its a:",labels[np.argmax(prediction)])

      #move the servo
      if labels[np.argmax(prediction)] == 'bluepill':
            servo1.angle = 90
            time.sleep(1)
            servo1.angle = 0
            break
      if labels[np.argmax(prediction)] == 'redpill':
            servo2.angle = 90
            time.sleep(1)
            servo2.angle = 0
            break

      if webCam:
         if sys.argv[-1] == "noWindow":
            cv2.imwrite('detected_out.jpg',img)
            continue
         cv2.imshow('detected (press q to quit)',img)
         if cv2.waitKey(1) & 0xFF == ord('q'):
            cap.release()
            break
      else:
         time.sleep(2)
         break

cv2.imwrite('detected_out.jpg',img)
cv2.destroyAllWindows() 
