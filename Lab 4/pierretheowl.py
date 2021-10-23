import time
import subprocess
import digitalio
import board
import busio
import adafruit_mpr121
import adafruit_rgb_display.st7789 as st7789
from PIL import Image, ImageDraw, ImageFont



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
disp.image(image, rotation)
# Draw some shapes.
# First define some constants to allow easy resizing of shapes.
padding = -2
top = padding
bottom = height - padding
# Move left to right keeping track of the current x position for drawing shapes.
x = 0

font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 20)
Intro1 = "I'm Pierre,"
Intro2 = "your French teacher"
x, y = 20, 20
draw.rectangle((0, 0, width, height), outline=0, fill=0)
draw.text((x, y), Intro1, font=font, fill="#FFFFFF")
y += font.getsize(Intro1)[1]
draw.text((x, y), Intro2, font=font, fill="#FFFFFF")
disp.image(image, rotation)


#initialize board and the touch sensor
i2c = busio.I2C(board.SCL, board.SDA)
mpr121 = adafruit_mpr121.MPR121(i2c)


#initialize Buttons
buttonA = digitalio.DigitalInOut(board.D23)
buttonB = digitalio.DigitalInOut(board.D24)
buttonA.switch_to_input()
buttonB.switch_to_input()

#set up the text2speak
def speak_eng(val):
    subprocess.run(["sh", "GoogleTTS_English.sh", val])

def speak_fr(val):
    subprocess.run(["sh", "GoogleTTS_French.sh", val])



#questions_level1
# vocabs = {"1":"Wine", "2":"Chocolate", "3":"Cheese", "4":"Bread", "5":"Water", "6":"Wine", "7":"Chocolate", "8":"Cheese", "9":"Bread", "10":"Water"}
vocabs = ['le vin','Chocolat','du formage','le pain','l\'eau']
question_num = [1,2,3,4,5]

# score for each player
score_blue = 0
score_orange = 0

def play(q_num):
    global score_blue
    global score_orange 

    player_blue = q_num +1 
    player_orange = q_num +6

    #play the question
    speak_fr(str(vocabs[q_num]))

    #font setting
    font2 = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 62)

    #score them
    while True:

        #play it one more time when the player presses one of the buttons
        if not buttonA.value or not buttonB.value:
            speak_fr(str(vocabs[q_num]))
    
        if mpr121[player_blue].value:
            score_blue = score_blue + 1
            speak_eng("player Blue, correct")
            print('player blue: ', score_blue)
            currentscore = str(score_blue) + " : " + str(score_orange)
            #print on the display
            draw.rectangle((0, 0, width, height), outline=0, fill=0)
            draw.text((50, 50), currentscore, font=font2, fill="#FFFFFF")
            disp.image(image, rotation)
            break 

        if mpr121[player_orange].value:
            score_orange = score_orange +1 
            speak_eng("player Orange, correct")
            print('plyer orange: ', score_orange)
            currentscore = str(score_blue) + " : " + str(score_orange)
            #print on the display
            draw.rectangle((0, 0, width, height), outline=0, fill=0)
            draw.text((50, 50), currentscore, font=font2, fill="#FFFFFF")
            disp.image(image, rotation)
            break
        


while True:

    if not buttonA.value or not buttonB.value:
        # speak_fr("Bonjour!")
        # speak_eng("I am Pierre the owl and I am going to teach you french.")
        # speak_eng("In this game, I will say a word in french and your task is to touch the corresponding word in english.")
        # speak_eng("The player who touches the english card first will get the point")
        # speak_eng("If you want to hear the french word again, press any button")
        speak_eng("Let's get started!")

        for i in range(2):
            play(i)

        print(score_blue, " : ", score_orange)
        if score_blue > score_orange:
            speak_eng("The winner is Player Blue")
        else:
            speak_eng("The winner is Player Orange")

        break

   
