import time 
from time import strftime, sleep
import subprocess
import digitalio
import board
from PIL import Image, ImageDraw, ImageFont
import adafruit_rgb_display.st7789 as st7789
from random import choice
from datetime import datetime, timedelta

#button
import qwiic_button 
import sys 



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

image2 = Image.open("eins.png").convert('RGB')

# Scale the image to the smaller screen dimension
image_ratio = image2.width / image2.height
screen_ratio = width / height
if screen_ratio < image_ratio:
    scaled_width = image2.width * height // image2.height
    scaled_height = height
else:
    scaled_width = width
    scaled_height = image2.height * width // image2.width
image2 = image2.resize((scaled_width, scaled_height), Image.BICUBIC)

# Crop and center the image
x = scaled_width // 2 - width // 2
y = scaled_height // 2 - height // 2
image2 = image2.crop((x, y, x + width, y + height))
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

#qwiic button _ green
my_button = qwiic_button.QwiicButton()


# Other 
Menu = [ "Salmon", "Steak", "Salad", "Last Delivery", "Fancy Meal", "Via Crota","Katz",
"Fasting!", "Korean", "Thai", "Pizza on 28th", "Cookshop", "Sandwich", "Soup" ,"HOTPOT",
"Ask Leo", "Egg-in-Hell","Cook A New Recipe","Wholefoods Deli"]


hour = int(strftime("%H"))
if hour >= 0 and hour < 1 or hour >= 23:
    animaltime = 'Time for Mice to run!'
    period_fill = "#003366"
elif hour >= 1 and hour < 3:
    animaltime = 'Cows chewing the cud nomnom'
    period_fill = "#000000"
elif hour >= 3 and hour < 5:
    animaltime = 'Tigers on hunt! Savage!'
    period_fill = "#000099"
elif hour >= 5 and hour < 7:
    animaltime = 'Rabbits in the moon!'
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
    animaltime = 'Piggies to go to bed'
    period_fill = "#003366"

while True:
#     # Draw a black filled box to clear the image.
    draw.rectangle((0, 0, width, height), outline=0, fill=0)
#
#   #TODO: Lab 2 part D work should be filled in here. You should be able to look in cli_clock.py and stats.py
    #positions
    y = height/3
    x = 0
    y2 = height/2.5
    x2 = width/5

    #main texts for display
    txt_top = "It's time for..."
    txt_bottom = "*press both at mealtime"


    draw.rectangle((0, 0, width, height), outline=0, fill=period_fill)
    draw.text((x2, y), txt_top, font=font, fill="#FFFFFF")
    y2 += font.getsize(txt_top)[1]
    x2 = width/6
    draw.text((x2, y2), animaltime, font=font, fill="#0000FF")
    y2 += (font.getsize(animaltime)[1])*2
    draw.text((x, y2), txt_bottom, font=font, fill="#808080")
    

    #reset the coordinates
    y = height/3
    y2 = height/2.5
    x2 = width/5
    
    if my_button.is_button_pressed() == True:
        disp.image(image2, rotation)
        
        # y = height/2.5
        # x = width/5
        # txt = str(my_button.time_since_last_click()/1000*200) + ' bee flaps'
        # txt1 = str(my_button.time_since_last_click()/1000) + ' seconds'
        
        
        # draw.rectangle((0, 0, width, height), outline=0, fill=0)
        # draw.text((x, y), txt, font=font, fill="#FFFF00")
        # y += font.getsize(txt)[1]
        # draw.text((x, y), txt1, font=font, fill="#808080")

    if buttonA.value and not buttonB.value:  # just button A pressed
        draw.rectangle((0, 0, width, height), outline=0, fill=0)
        TIME = "ON THE OTHER SIDE: " 
        SeoulTime= datetime.now() + timedelta(hours=13)
        LondonTime= datetime.now() + timedelta(hours=5)
        SEL="Seoul: " + format(SeoulTime, '%a %p%H:%M:%S') 
        LON="London: "+ format(LondonTime, '%a %p%H:%M:%S') 
        draw.text((x,y), TIME, font=font, fill="#FFFFFF")
        y += font.getsize(TIME)[1]
        draw.text((x, y), SEL, font=font, fill="#FFFFFF")
        y += font.getsize(SEL)[1]
        draw.text((x, y), LON, font=font, fill="#FFFFFF")

    if buttonB.value and not buttonA.value:  # just button B pressed
        draw.rectangle((0, 0, width, height), outline=0, fill=0)
        TIME = "HERE, NOW: " 
        txt1 = strftime("%m/%d %a %p%H:%M:%S")

        # draw.text((x, y), txt0, font=font, fill="#FFFFFF")
        # y += font.getsize(txt0)[1]
        draw.text((x, y), TIME, font=font, fill="#FFFFFF")
        y += font.getsize(TIME)[1]
        draw.text((x2, y), txt1, font=font, fill="#FFFFFF")


    if not buttonA.value and not buttonB.value:  # both pressed
        draw.rectangle((0, 0, width, height), outline=0, fill=0)
        Whattoeat = choice(Menu)
        txt = "Today's menu:"
        draw.text((x2, y2), txt, font=font, fill="#FFFF00")
        y2 += font.getsize(txt)[1]
        draw.text((x2, y2), Whattoeat, font=font, fill="#FFFFFF")

    # Display image.
    disp.image(image, rotation)
    time.sleep(1)










