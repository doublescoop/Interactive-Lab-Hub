import time
import subprocess
import digitalio
import board
from PIL import Image, ImageDraw, ImageFont
import adafruit_rgb_display.st7789 as st7789
import busio
from adafruit_apds9960.apds9960 import APDS9960
import time
import qwiic_button
import sys
import digitalio
import os
from vosk import Model, KaldiRecognizer
import wave
import json
import shlex
from subprocess import Popen, call

# Configuration for CS and DC pins (these are FeatherWing defaults on M0/M4):
cs_pin = digitalio.DigitalInOut(board.CE0)
dc_pin = digitalio.DigitalInOut(board.D25)
reset_pin = None

# Config for display baudrate (default max is 24mhz):
BAUDRATE = 64000000

# Setup SPI bus using hardware SPI:
spi = board.SPI()

# Create the ST7789 display:
disp = st7789.ST7789(
    spi,
    cs=cs_pin,
    dc=dc_pin,
    rst=reset_pin,
    baudrate=BAUDRATE,
    width=135,
    height=240,
    x_offset=53,
    y_offset=40,
)

# Create blank image for drawing.
# Make sure to create image with mode 'RGB' for full color.
height = disp.width  # we swap height/width to rotate it to landscape!
width = disp.height
image = Image.new("RGB", (width, height))
rotation = 90

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0, 0, width, height), outline=0, fill=(0, 0, 0))

# Display the image
disp.image(image, rotation)

# Turn on the backlight
backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True

# Initialize the buttons on the screen
buttonA = digitalio.DigitalInOut(board.D23)
buttonB = digitalio.DigitalInOut(board.D24)
buttonA.switch_to_input()
buttonB.switch_to_input()

# Initialize Green LED to visually signal players
# when they're correct
buttonG = qwiic_button.QwiicButton()


# Initialize accelerometer
# i2c = busio.I2C(board.SCL, board.SDA)
# mpu = adafruit_mpu6050.MPU6050(i2c)
# address = 0x68

# Initialize proximity sensor to initiate the interaction
i2c = board.I2C()  # uses board.SCL and board.SDA
sensor = APDS9960(i2c)
sensor.enable_proximity = True


def speak(val):
    subprocess.run(["sh", "GoogleTTS_demo.sh", val])


def check_userinput():
    os.system("arecord -D hw:2,0 -f cd -c1 -r 48000 -d 4 -t wav recorded_mono.wav")
    wf = wave.open("recorded_mono.wav", "rb")

    model = Model("model")
    # rec = KaldiRecognizer(model, wf.getframerate())
    rec = KaldiRecognizer(model, wf.getframerate())
    #'["black","beige","blue","brown","green","grey","navy","orange","red","yellow","yes","start"," [unk]"]')

    while True:
        data = wf.readframes(4000)
        if len(data) == 0:
            break
        rec.AcceptWaveform(data)

    reply = json.loads(rec.FinalResult())
    print("User's reply: ", reply["text"])
    return reply["text"]


# def stopwatch(seconds):
#     start = time.time()
#     time.clock()
#     elapsed = 0
#     while elapsed < seconds:
#         elapsed = time.time() - start
#         print ("loop cycle time: %f, seconds count: %02d % (time.clock() , elapsed)")
#         time.sleep(1)
#     return elapsed


score = 0

while True:
    prox = sensor.proximity
    if prox > 10:
        main_image = Image.open("images/a_hi.png")
        main_image = main_image.convert("RGB")
        main_image = main_image.resize((width, height), Image.BICUBIC)
        disp.image(main_image, rotation)
        speak("Hi there boo!")
        time.sleep(2)
        break

# begin interaction when picked up
# while True:
#     gyro = mpu.gyro
#     if gyro == 0.0:
#         speak("Hi, pick me up! pick me up! ... Pat me, Pick me up!")
#         if gyro != 0.0:
#             break

while True:
    main_image = Image.open("images/a_boo.png")
    main_image = main_image.convert("RGB")
    main_image = main_image.resize((width, height), Image.BICUBIC)
    disp.image(main_image, rotation)
    # ask name and test microphone
    speak("Thank you for waking me up. I'm boo. What is your name?")
    reply_name = check_userinput()
    if len(reply_name) > 1:
        speak(str(reply_name))
        speak("What is your hobby?")
    else:
        speak(
            "Please speak louder to the microphon on the side, like get really really close to me. what is your name again?"
        )
        reply_name = check_userinput()
        speak(str(reply_name))
        speak("What is your hobby?")

    # ask hobby and initiate the game
    reply_hobby = check_userinput()
    if len(reply_hobby) > 1:
        speak(str(reply_hobby))
        speak(
            "That's interesting. I like to draw. Do you want to see my drawings and guess what they are?"
        )
    else:
        speak(
            "I didn't hear you well. anyhow, my hobby is drawing. Do you want to see my drawings and guess what they are?"
        )

    reply_start = check_userinput()
    if "yes" or "sure" or "okay" or "good" or "cool" in reply_start:
        speak(
            "cool! I have six pics. Guess in three seconds. Say only once, very close to the microphone on the bottom right. \
            It will warm my heart up if you get my drawings"
        )
        draw.rectangle((0, 0, width, height), outline=0, fill=0)
        q1 = Image.open("images/a_intro.png")
        q1 = q1.convert("RGB")
        q1 = q1.resize((width, height), Image.BICUBIC)
        disp.image(q1, rotation)
        time.sleep(2)
        # Draw a black filled box to clear the image.
        draw.rectangle((0, 0, width, height), outline=0, fill=0)
        q1 = Image.open("images/04_snowman.png")
        q1 = q1.convert("RGB")
        q1 = q1.resize((width, height), Image.BICUBIC)
        disp.image(q1, rotation)
        time.sleep(1)
        reply = check_userinput()
        if "snow man" in reply or "snowman" in reply:
            score += 1
            buttonG.LED_on(150)
            speak("correct, my heart is warmed")
            buttonG.LED_off()
        else:
            speak("wrong, it's snowman.")

        speak("next")
        q2 = Image.open("images/02_icecream.png")
        q2 = q2.convert("RGB")
        q2 = q2.resize((width, height), Image.BICUBIC)
        disp.image(q2, rotation)
        time.sleep(1)
        reply = check_userinput()
        if "icecream" or "ice cream" or "i scream" in reply:
            score += 1
            buttonG.LED_on(150)
            speak("correct")
            buttonG.LED_off()
        else:
            speak("wrong, it's icecream")

        speak("next")
        q3 = Image.open("images/08_beach.png").convert("RGB")
        q3 = q3.resize((width, height), Image.BICUBIC)
        disp.image(q3, rotation)
        time.sleep(1)
        reply = check_userinput()
        if "beach" in reply:
            score += 1
            buttonG.LED_on(150)
            speak("correct")
            buttonG.LED_off()
        else:
            speak("wrong, it's a beach.")

        speak("next")
        q4 = Image.open("images/05_yoga.png").convert("RGB")
        q4 = q4.resize((width, height), Image.BICUBIC)
        disp.image(q4, rotation)
        time.sleep(1)
        reply = check_userinput()
        if "yoga" in reply:
            score += 1
            buttonG.LED_on(150)
            speak("correct")
            buttonG.LED_off()
        else:
            speak("wrong, I drew yoga")

        speak("next")
        q5 = Image.open("images/09_hotdog.png").convert("RGB")
        q5 = q5.resize((width, height), Image.BICUBIC)
        disp.image(q5, rotation)
        time.sleep(1)
        reply = check_userinput()
        if "hot dog" in reply:
            score += 1
            buttonG.LED_on(150)
            speak("correct, my heart is warmed")
            buttonG.LED_off()
        else:
            speak("wrong, it's hotdog")

        speak("next")
        q6 = Image.open("images/10_asparagus.png").convert("RGB")
        q6 = q6.resize((width, height), Image.BICUBIC)
        disp.image(q6, rotation)
        time.sleep(1)
        reply = check_userinput()
        if "asparagus" in reply:
            score += 1
            buttonG.LED_on(150)
            speak("correct")
            buttonG.LED_off()
        else:
            speak("wrong, it's asparagus")

        #announces total score and give comments accordingly
        speak("your score is" + str(score))
        if score < 3:
            speak("you don't get my drawings")
        elif score >= 3 and score < 6:
            speak("You are pretty good")
        elif score == 6:
            speak("oh my god you must be my soulmate")

    else:
        speak("I assume you don't want to play with me.")
        time.sleep(1)
        break

    speak("bye, let's play next time")
    end = Image.open("images/end.png").convert("RGB")
    end = end.resize((width, height), Image.BICUBIC)
    disp.image(end, rotation)
    time.sleep(1)

    break
