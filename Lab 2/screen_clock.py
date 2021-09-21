import time 
from time import strftime, sleep
import subprocess
import digitalio
import board
from PIL import Image, ImageDraw, ImageFont
import adafruit_rgb_display.st7789 as st7789
from random import choice
import pytz, datetime
from datetime import datetime, timedelta


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
disp.image(image, rotation)
# Draw some shapes.
# First define some constants to allow easy resizing of shapes.
padding = -2
top = padding
bottom = height - padding
# Move left to right keeping track of the current x position for drawing shapes.
x = 0

# Alternatively load a TTF font.  Make sure the .ttf font file is in the
# same directory as the python script!
# Some other nice fonts to try: http://www.dafont.com/bitmap.php
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSerifCondensed.ttf", 18)

# Turn on the backlight
backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True

#button settings
buttonA = digitalio.DigitalInOut(board.D23)
buttonB = digitalio.DigitalInOut(board.D24)
buttonA.switch_to_input()
buttonB.switch_to_input()


# Other 
Menu = [ "Salmon", "Steak", "Salad", "Last Delivery", "Fancy Meal", "Via Crota","Katz",
"Fasting!", "Korean", "Thai", "Pizza on 28th", "Cookshop", "Sandwich", "Soup" ,"HOTPOT",
"Ask Leo", "Egg-in-Hell","Cook A New Recipe","Wholefoods Deli"]

while True:
#     # Draw a black filled box to clear the image.
    draw.rectangle((0, 0, width, height), outline=0, fill=0)
#
#     #TODO: Lab 2 part D work should be filled in here. You should be able to look in cli_clock.py and stats.py
    y = top 

    txt0 = "What Time Is It?"
    TIME = "HERE, NOW: " + strftime("%m/%d %H:%M:%S")
    txt1 = "in 18C?"
    txt2 = "on the other side?"
    txt3 = "*press both at mealtime"

    draw.text((x, y), txt0, font=font, fill="#FFFFFF")
    y += font.getsize(txt0)[1]
    draw.text((x, y), TIME, font=font, fill="#FFFFFF")
    y += font.getsize(TIME)[1]
    draw.text((x, y), txt1, font=font, fill="#cde494")
    y += font.getsize(txt1)[1]
    draw.text((x, y), txt2, font=font, fill="#cde494")
    y += font.getsize(txt2)[1] 
    draw.text((x, y), txt3, font=font, fill="#333333")


    hour = int(strftime("%H"))
    if hour >= 0 and hour < 1 or hour >= 23:
        animaltime = 'Time for Mice to run around!'
        period_fill = "#003366"
    elif hour >= 1 and hour < 3:
        animaltime = 'Cows chewing the cud nomnom'
        period_fill = "#000000"
    elif hour >= 3 and hour < 5:
        animaltime = 'Tigers on hunt! Savage!'
        period_fill = "#000099"
    elif hour >= 5 and hour < 7:
        animaltime = 'Are there Rabbits in the moon?'
        period_fill = "#000099"
    elif hour >= 7 and hour < 9:
        animaltime = 'Dragons getting ready to FLY'
        period_fill = "#9999CC"
    elif hour >= 9 and hour < 11:
        animaltime = 'Snakes are sleeping, you\'re safe'
        period_fill = "#FFCC00"
    elif hour >= 11 and hour < 13:
        animaltime = 'Horses run wild ==3'
        period_fill = "#FFCC00"
    elif hour >= 13 and hour < 15:
        animaltime = 'Sheep having long lunch'
        period_fill = "#FFCC00"
    elif hour >= 15 and hour < 17:
        animaltime = 'Monkeys party loud'
        period_fill = "#FF9900"
    elif hour >= 17 and hour < 19:
        animaltime = 'Hens heading back home'
        period_fill = "#FF9900"
    elif hour >= 19 and hour < 21:
        animaltime = 'Dogs on guard!'
        period_fill = "#003366"
    elif hour >= 21 and hour < 23:
        animaltime = 'Time for piggies to go to bed'
        period_fill = "#003366"


    # timeUTC = datetime.datetime.now()
    # timezoneLocal = pytz.timezone('Asia/Seoul')
    # utc = pytz.utc
    # timeLocal = utc.localize(timeUTC).astimezone(timezoneLocal)
    # SeoulTime= datetime.now() + timedelta(hours=13)
    # SEL="future: " + format(SeoulTime, '%a %p%H:%M:%S')
    
    y2 = height/2.5
    x2 = 2
    


    if buttonA.value and not buttonB.value:  # just button A pressed
        SeoulTime= datetime.now() + timedelta(hours=13)
        LondonTime= datetime.now() + timedelta(hours=5)
        SEL="Seoul: " + format(SeoulTime, '%a %p%H:%M:%S') 
        LON="London: "+ format(LondonTime, '%a %p%H:%M:%S') 
        draw.rectangle((0, 0, width, height), outline=0, fill=0)
        draw.text((x, y), SEL, font=font, fill="#FFFFFF")
        y += font.getsize(SEL)[1]
        draw.text((x2, y), LON, font=font, fill="#FFFFFF")
    if buttonB.value and not buttonA.value:  # just button B pressed
        draw.rectangle((0, 0, width, height), outline=0, fill=period_fill)
        draw.text((x2, y2), animaltime, font=font, fill="#0000FF")
    if not buttonA.value and not buttonB.value:  # both pressed
        Whattoeat = choice(Menu)
        txt = "Today's menu:"
        draw.rectangle((0, 0, width, height), outline=0, fill=0)
        draw.text((x2, y2), txt, font=font, fill="#FFFF00")
        y += font.getsize(txt)[1]
        draw.text((x2, y), Whattoeat, font=font, fill="#FFFFFF")


 # Display image.
    disp.image(image, rotation)
    time.sleep(1)
