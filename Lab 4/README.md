# Ph-UI!!!

For lab this week, we focus on both on sensing, to bring in new modes of input into your devices, as well as prototyping the physical look and feel of the device. You will think about the physical form the device needs to perform the sensing as well as present the display or feedback about what was sensed. 

## Part 1 Lab Preparation

### Get the latest content:
As always, pull updates from the class Interactive-Lab-Hub to both your Pi and your own GitHub repo. As we discussed in the class, there are 2 ways you can do so:

**\[recommended\]**Option 1: On the Pi, `cd` to your `Interactive-Lab-Hub`, pull the updates from upstream (class lab-hub) and push the updates back to your own GitHub repo. You will need the personal access token for this.

```
pi@ixe00:~$ cd Interactive-Lab-Hub
pi@ixe00:~/Interactive-Lab-Hub $ git pull upstream Fall2021
pi@ixe00:~/Interactive-Lab-Hub $ git add .
pi@ixe00:~/Interactive-Lab-Hub $ git commit -m "get lab4 content"
pi@ixe00:~/Interactive-Lab-Hub $ git push
```

Option 2: On your your own GitHub repo, [create pull request](https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/blob/2021Fall/readings/Submitting%20Labs.md) to get updates from the class Interactive-Lab-Hub. After you have latest updates online, go on your Pi, `cd` to your `Interactive-Lab-Hub` and use `git pull` to get updates from your own GitHub repo.

### Start brasinstorming ideas by reading: 
* [What do prototypes prototype?](https://www.semanticscholar.org/paper/What-do-Prototypes-Prototype-Houde-Hill/30bc6125fab9d9b2d5854223aeea7900a218f149)
* [Paper prototyping](https://www.uxpin.com/studio/blog/paper-prototyping-the-practical-beginners-guide/) is used by UX designers to quickly develop interface ideas and run them by people before any programming occurs. 
* [Cardboard prototypes](https://www.youtube.com/watch?v=k_9Q-KDSb9o) help interactive product designers to work through additional issues, like how big something should be, how it could be carried, where it would sit. 
* [Tips to Cut, Fold, Mold and Papier-Mache Cardboard](https://makezine.com/2016/04/21/working-with-cardboard-tips-cut-fold-mold-papier-mache/) from Make Magazine.
* [Surprisingly complicated forms](https://www.pinterest.com/pin/50032245843343100/) can be built with paper, cardstock or cardboard.  The most advanced and challenging prototypes to prototype with paper are [cardboard mechanisms](https://www.pinterest.com/helgangchin/paper-mechanisms/) which move and change. 
* [Dyson Vacuum Cardboard Prototypes](http://media.dyson.com/downloads/JDF/JDF_Prim_poster05.pdf)
<p align="center"><img src="https://dysonthedesigner.weebly.com/uploads/2/6/3/9/26392736/427342_orig.jpg"  width="200" > </p>

### Gathering materials for this lab:

* Cardboard (start collecting those shipping boxes!)
* Found objects and materials--like bananas and twigs.
* Cutting board
* Cutting tools
* Markers

(We do offer shared cutting board, cutting tools, and markers on the class cart during the lab, so do not worry if you don't have them!)

## Deliverables \& Submission for Lab 4

The deliverables for this lab are, writings, sketches, photos, and videos that show what your prototype:
* "Looks like": shows how the device should look, feel, sit, weigh, etc.
* "Works like": shows what the device can do.
* "Acts like": shows how a person would interact with the device.

For submission, the readme.md page for this lab should be edited to include the work you have done:
* Upload any materials that explain what you did, into your lab 4 repository, and link them in your lab 4 readme.md.
* Link your Lab 4 readme.md in your main Interactive-Lab-Hub readme.md. 
* Group members can turn in one repository, but make sure your Hub readme.md links to the shared repository.
* Labs are due on Mondays, make sure to submit your Lab 4 readme.md to Canvas.


## Lab Overview

A) [Capacitive Sensing](#part-a)

B) [OLED screen](#part-b) 

C) [Paper Display](#part-c)

D) [Materiality](#part-d)

E) [Servo Control](#part-e)

F) [Record the interaction](#part-f)

## The Report (Part 1: A-D, Part 2: E-F)

### Part A
### Capacitive Sensing, a.k.a. Human-Twizzler Interaction 

We want to introduce you to the [capacitive sensor](https://learn.adafruit.com/adafruit-mpr121-gator) in your kit. It's one of the most flexible input devices we are able to provide. At boot, it measures the capacitance on each of the 12 contacts. Whenever that capacitance changes, it considers it a user touch. You can attach any conductive material. In your kit, you have copper tape that will work well, but don't limit yourself! In the example below, we use Twizzlers--you should pick your own objects.


<p float="left">
<img src="https://cdn-learn.adafruit.com/guides/cropped_images/000/003/226/medium640/MPR121_top_angle.jpg?1609282424" height="150" />
<img src="https://cdn-shop.adafruit.com/1200x900/4401-01.jpg" height="150">
</p>

Plug in the capacitive sensor board with the QWIIC connector. Connect your Twizzlers with either the copper tape or the alligator clips (the clips work better). In this lab, we will continue to use the `circuitpython` virtual environment we created before. Activate `circuitpython` and `cd` to your Lab 4 folder to install the requirements by:

```
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 4 $ pip3 install -r requirements.txt
```

<img src="https://media.discordapp.net/attachments/679721816318803975/823299613812719666/PXL_20210321_205742253.jpg" width=400>
These Twizzlers are connected to pads 6 and 10. When you run the code and touch a Twizzler, the terminal will print out the following

```
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 4 $ python cap_test.py 
Twizzler 10 touched!
Twizzler 6 touched!
```

### Part B
### More sensors

#### Light/Proximity/Gesture sensor (APDS-9960)

We here want you to get to know this awesome sensor [Adafruit APDS-9960](https://www.adafruit.com/product/3595). It is capable of sensing proximity, light (also RGB), and gesture! 

<img src="https://cdn-shop.adafruit.com/970x728/3595-03.jpg" width=200>

Connect it to your pi with Qwiic connector and try running the three example scripts individually to see what the sensor is capable of doing!

```
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 4 $ python proximity_test.py
...
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 4 $ python gesture_test.py
...
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 4 $ python color_test.py
...
```

You can go the the [Adafruit GitHub Page](https://github.com/adafruit/Adafruit_CircuitPython_APDS9960) to see more examples for this sensor!

#### Rotary Encoder

A rotary encoder is an electro-mechanical device that converts the angular position to analog or digital output signals. The [Adafruit rotary encoder](https://www.adafruit.com/product/4991#technical-details) we ordered for you came with separated breakout board and encoder itself, that is, they will need to be soldered if you have not yet done so! We will be bringing the soldering station to the lab class for you to use, also, you can go to the MakerLAB to do the soldering off-class. Here is some [guidance on soldering](https://learn.adafruit.com/adafruit-guide-excellent-soldering/preparation) from Adafruit. When you first solder, get someone who has done it before (ideally in the MakerLAB environment). It is a good idea to review this material beforehand so you know what to look at.

<p float="left">
<img src="https://cdn-shop.adafruit.com/970x728/4991-01.jpg" height="200" />
<img src="https://cdn-shop.adafruit.com/970x728/377-02.jpg" height="200" />
<img src="https://cdn-shop.adafruit.com/970x728/4991-09.jpg" height="200">
</p>

Connect it to your pi with Qwiic connector and try running the example script, it comes with an additional button which might be useful for your design!

```
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 4 $ python encoder_test.py
```

You can go to the [Adafruit Learn Page](https://learn.adafruit.com/adafruit-i2c-qt-rotary-encoder/python-circuitpython) to learn more about the sensor! The sensor actually comes with an LED (neo pixel): Can you try lighting it up? 

#### Joystick

A [joystick](https://www.sparkfun.com/products/15168) can be used to sense and report the input of the stick for it pivoting angle or direction. It also comes with a button input!

<p float="left">
<img src="https://cdn.sparkfun.com//assets/parts/1/3/5/5/8/15168-SparkFun_Qwiic_Joystick-01.jpg" height="200" />
</p>

Connect it to your pi with Qwiic connector and try running the example script to see what it can do!

```
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 4 $ python joystick_test.py
```

You can go to the [SparkFun GitHub Page](https://github.com/sparkfun/Qwiic_Joystick_Py) to learn more about the sensor!

#### (Optional) Distance Sensor

Note: We did not distribute this sensor to you, so if you are interested in playing with it, please come pick it up from the TA!

Earlier we have asked you to play with the proximity sensor, which is able to sense object within a short distance. Here, we offer [Qwiic Multi Distance Sensor](https://www.sparkfun.com/products/17072), which has a field of view of about 25° and is able to detect objects up to 3 meters away! 

<p float="left">
<img src="https://cdn.sparkfun.com//assets/parts/1/6/0/3/4/17072-Qwiic_Multi_Distance_Sensor_-_VL53L3CX-01.jpg" height="200" />
</p>

Connect it to your pi with Qwiic connector and try running the example script to see how it works!

```
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 4 $ python distance_test.py
```

You can go to the [SparkFun GitHub Page](https://github.com/sparkfun/Qwiic_VL53L1X_Py) to learn more about the sensor and see other examples!

### Part C
### Physical considerations for sensing

Usually, sensors need to positioned in specific locations or orientations to make them useful for their application. Now that you've tried a bunch of the sensors, pick one that you would like to use, and an application where you use the output of that sensor for an interaction. For example, you can use a distance sensor to measure someone's height if you position it overhead and get them to stand under it.

**\*\*\*Draw 5 sketches of different ways you might use your sensor, and how the larger device needs to be shaped in order to make the sensor useful.\*\*\***

**\*\*\*What are some things these sketches raise as questions? What do you need to physically prototype to understand how to anwer those questions?\*\*\***

Idea 1: Distance sensors in the floor at a store to alert people if they are standing closer then 6 feet to one another. 
The larger device is the system of both the sensor in the floor and a speaker on the ceiling. The floor sensors will be 6 feet a part and notify the speaker to beep if they sense someone has broken the 6 feet rule. 
![idea1](https://user-images.githubusercontent.com/73661058/137837271-6d212f9f-f9a4-41c8-8bf4-cd2580f4a9bf.jpg)

- Where should the distance sensor be positioned physically in various store setting so it can effectively measure the distance between the people in line? 
 > a prototype of an attachable sensor design that can easily be re-positioned. The size, weight, and angle to measure the distance would be critical in this prototype.

Idea 2: Touch sensors under a chair to detect when a person sits down at their desk thier lamp turns on.
The larger device is the system of both the sensor on the chair and the lamp. The touch sensor will detect the touch of someone sitting down and it will communicate withe the light when it detects touch. 
![idea2](https://user-images.githubusercontent.com/73661058/137837501-1f5aa437-8846-40de-91ca-c4e4a80a5240.jpg)

- Would the user seating on a chair feel like the sensor on the bottom uncomfortable? How can we make the device not physically disturbing to the user but still positioned in the most effective spot(e.g. right under the seating area of chair)? 
 > a prototype with different coverings of the sensor which can test how the user feel when they're sitting on it. building with an actual chair and positioning them in different spots can be helpful too. 

Idea 3: This is idea is an interactive story book. As a child reads through a book they can touch the images and they will come to live in animation in a near by monitor. The story book would be made out of conductive material attached to touch sensor to detect when a particular image is touched. When the sensor detcts touch it would communicate with the monitor and on what animation to display. 
![idea3](https://user-images.githubusercontent.com/73661058/137838174-56edf778-a1ea-4873-a200-13f3c7eab51a.jpg)

- How can the touch sensors be attatched to a book but not disturb the reader? How can we section out certain part of the page to be connected with a specific sensor?
 > a prototype of an interactive book that each page is thick enough to hold the sensors. Explore with different conductive materials that can be easily attatched to the pages for the sensors. 

Idea 4: This idea is a language learning game. The decive says a word in french and the players task is to touch the corresponding connected word in english. The Pi and speaker will be in a box with touch sensors connected attached to connective buttons the user can touch. 
![idea4](https://user-images.githubusercontent.com/73661058/137839198-1eb78e94-e861-4689-9f5e-af8a4a574e06.jpg)

- What kind of casing is needed to cover the device and make all the wires look neater? What kind of conductive material should be used? What size of the panel is appropriate?
 > a prototype to explore different size and material of the casing and the panel. 

Idea 5: This is a yoga alram clock. Users must walk up to the alram clock and do a yoga pose for it to shut it up. The larger device must use motion sensors and pose recognition in its design to sense when to quiet itself. The larger device will also have a speaker to scream at the user to wake up. 
![idea5](https://user-images.githubusercontent.com/73661058/137839680-06d7a7e7-922b-4694-bc22-ebe81474f4a4.jpg)

- What is the best way to implement the motion detection/pose recognition? What is a good pose that's moderately hard for the users (so they can be awoke) and easy for the sensor to recognize? What is the appropriate distance? Where should the camera be placed in the clock?
> a prototype to test the recognition functions and to determine the place for the camera.


- What is the best way to implement the motion detection/pose recognition? What is a good pose that's moderately hard for the users (so they can be awoke) and easy for the sensor to recognize? What is the appropriate distance? Where should the camera be placed in the clock?
> a prototype to test the recognition functions and to determine the place for the camera. 

**\*\*\*Pick one of these designs to prototype.\*\*\***


### Part D
### Physical considerations for displaying information and housing parts


Here is an Pi with a paper faceplate on it to turn it into a display interface:

<img src="https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/blob/2020Fall/images/paper_if.png?raw=true"  width="250"/>


This is fine, but the mounting of the display constrains the display location and orientation a lot. Also, it really only works for applications where people can come and stand over the Pi, or where you can mount the Pi to the wall.

Here is another prototype for a paper display:

<img src="https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/blob/2020Fall/images/b_box.png?raw=true"  width="250"/>

Your kit includes these [SparkFun Qwiic OLED screens](https://www.sparkfun.com/products/17153). These use less power than the MiniTFTs you have mounted on the GPIO pins of the Pi, but, more importantly, they can be more flexibily be mounted elsewhere on your physical interface. The way you program this display is almost identical to the way you program a  Pi display. Take a look at `oled_test.py` and some more of the [Adafruit examples](https://github.com/adafruit/Adafruit_CircuitPython_SSD1306/tree/master/examples).

<p float="left">
<img src="https://cdn.sparkfun.com//assets/parts/1/6/1/3/5/17153-SparkFun_Qwiic_OLED_Display__0.91_in__128x32_-01.jpg" height="200" />
<img src="https://cdn.discordapp.com/attachments/679466987314741338/823354087105101854/PXL_20210322_003033073.jpg" height="200">
</p>


It holds a Pi and usb power supply, and provides a front stage on which to put writing, graphics, LEDs, buttons or displays.

This design can be made by scoring a long strip of corrugated cardboard of width X, with the following measurements:

| Y height of box <br> <sub><sup>- thickness of cardboard</sup></sub> | Z  depth of box <br><sub><sup>- thickness of cardboard</sup></sub> | Y height of box  | Z  depth of box | H height of faceplate <br><sub><sup>* * * * * (don't make this too short) * * * * *</sup></sub>|
| --- | --- | --- | --- | --- | 

Fold the first flap of the strip so that it sits flush against the back of the face plate, and tape, velcro or hot glue it in place. This will make a H x X interface, with a box of Z x X footprint (which you can adapt to the things you want to put in the box) and a height Y in the back. 

Here is an example:

<img src="https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/blob/2020Fall/images/horoscope.png?raw=true"  width="250"/>

Think about how you want to present the information about what your sensor is sensing! Design a paper display for your project that communicates the state of the Pi and a sensor. Ideally you should design it so that you can slide the Pi out to work on the circuit or programming, and then slide it back in and reattach a few wires to be back in operation.
 
**\*\*\*Sketch 5 designs for how you would physically position your display and any buttons or knobs needed to interact with it.\*\*\***
**\*\*\*What are some things these sketches raise as questions? What do you need to physically prototype to understand how to anwer those questions?\*\*\***

![deisgn1](https://user-images.githubusercontent.com/42717070/137841043-c7e6e443-4b2a-4112-8778-99bbfe65eec6.jpg)
This sketch raises the question of what material should we use for the buttons attached to the touch sensors. We know that we need to use something conductive so we thought to use some sort of aluminium. 

![design2](https://user-images.githubusercontent.com/42717070/137841047-7c226843-5e44-497c-915b-b934a7d8f955.jpg)
This sketch also raised questions about what materials we should use for the buttons or knobs in the design. We choose to go with the classic choice twizzlers. These would be stuck through holes in a cardboard game board and connected with alligator clips underneath the board. We also wanted to incorporate a cool design/mascot into the decive, we chose to use an owl. This raised questions of how we could make this structurally work. To answer this question our idea was to put the pi behind the owl display. 
![design3](https://user-images.githubusercontent.com/42717070/137841052-2a1fe736-fbcf-4bd7-89bb-f75633074073.jpg)
In this sketch we wanted to explore using a mode of communication with the users different than voice. To do this we choose to display the french would instead of speaking it to the user. We were questions with how could we do this in a creative way, we choose to make the display look like a dictionary.
![design4](https://user-images.githubusercontent.com/42717070/137841057-0219b587-2329-434b-9906-99221104aeb8.jpg)
We were exploring the right look and feel for a gamified interactive learning device, and we chose the look of an owl teacher!(a.k.a. Pierre the Owl) It raised question around the layouts of the owl, speaker, display, and the touch panels. We will need a physical prototype to configure the size and layouts. 
![design5](https://user-images.githubusercontent.com/42717070/137841062-c714e68d-0aa3-467f-9992-600a7daaad0b.jpg)
In this sketch we expanded the idea to use combbined playboards(instead of 10 panels) for each player. It raised questions about how to connect each words on the same board separately to each touch sensor outlet for each player. Physical prototyping for the board & cord placement, and exploring the conductive matertials would be important. 


**\*\*\*Pick one of these display designs to integrate into your prototype.\*\*\***

We decided to prototype the design 4. 

**\*\*\*Explain the rationale for the design.\*\*\*** (e.g. Does it need to be a certain size or form or need to be able to be seen from a certain distance?)

We are designing a gamified interactive language learning device. The device will speak in French and two players can compete to choose the corresponding English word faster, by touching panels with letters on them. We are using Pierre the Owl as our mascot to highlight the gamification feeling and foster the user engagement. He will be standing on the device, facing the users. A speaker to play French words/sentences and a display to show the score are needed to be placed near him. Since this device need the Pi, a display panel, the speaker, the touch sensor with 10 alligator clips, we decided to build a box casing around them to make the look neater. Players are expected to touch one of the five panels as fast as possible once the French word is played. So each panel has to be big enough for the user to comfortable touch them in fast motion, and the words on them should be big enough to be readable from an arm-length away. To incorporate two levels of the game, we designed the word panels to be reversible(the flipped side can be used for a different level). Panels should be made in materials easily flippable and have obvious two sides(it cannot be cylinder like a Twizzler). 


Build a cardbord prototype of your design.


**\*\*\*Document your rough prototype.\*\*\***

![proto1](https://user-images.githubusercontent.com/42717070/137850267-cdd95489-349c-4e34-8cb9-5471eecb6a6d.jpg)
![proto2](https://user-images.githubusercontent.com/42717070/137850270-f64e4370-3612-4f62-bf45-97b74e053556.jpg)
![proto_closeup](https://user-images.githubusercontent.com/42717070/137850264-b47fef91-2fb5-4798-bdcd-d2f97b2fe7b6.jpg)
![proto_inside](https://user-images.githubusercontent.com/42717070/137850265-a577ed70-ecfc-423d-b529-07d7bd583cc5.jpg)


LAB PART 2

### Part 2

Following exploration and reflection from Part 1, complete the "looks like," "works like" and "acts like" prototypes for your design, reiterated below.

### Part E (Optional)
### Servo Control with Joystick

In the class kit, you should be able to find the [Qwiic Servo Controller](https://www.sparkfun.com/products/16773) and [Micro Servo Motor SG51](https://www.adafruit.com/product/2201). The Qwiic Servo Controller will need external power supply to drive, which we will be distributing the battery packs in the class. Connect the servo controller to the miniPiTFT through qwiic connector and connect the external battery to the 2-Pin JST port (ower port) on the servo controller. Connect your servo to channel 2 on the controller, make sure the brown is connected to GND and orange is connected to PWM.

<img src="https://scontent-lga3-1.xx.fbcdn.net/v/t1.15752-9/245605956_303690921194525_3309212261588023460_n.jpg?_nc_cat=110&ccb=1-5&_nc_sid=ae9488&_nc_ohc=FvFLlClTKuUAX9nJ3LR&_nc_ht=scontent-lga3-1.xx&oh=b7ec1abc8d458b6c1b7a00a6f11398ac&oe=618D7D96" width="400"/>

In this exercise, we will be using the nice [ServoKit library](https://learn.adafruit.com/16-channel-pwm-servo-driver/python-circuitpython) developed by Adafruit! We will continue to use the `circuitpython` virtual environment we created. Activate the virtual environment and make sure to install the latest required libraries by running:

```
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 4 $ pip3 install -r requirements.txt
```

A servo motor is a rotary actuator or linear actuator that allows for precise control of angular or linear position. The position of a servo motor is set by the width of an electrical pulse, that is, we can use PWM (pulse-width modulation) to set and control the servo motor position. You can read [this](https://learn.adafruit.com/adafruit-arduino-lesson-14-servo-motors/servo-motors) to learn a bit more about how exactly a servo motor works.

Now that you have a basic idea of what a servo motor is, look into the script `qwiic_servo_example.py` we provide. In line 14, you should see that we have set up the min_pulse and max_pulse corresponding to the servo turning 0 - 180 degree. Try running the servo example code now and see what happens:

```
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 4 $ python servo_test.py
```

It is also possible to control the servo using the sensors mentioned in as in part A and part B, and/or from some of the buttons or parts included in your kit, the simplest way might be to chain Qwiic buttons to the other end of the Qwiic OLED. Like this:

<p align="center"> <img src="chaining.png"  width="200" ></p>

You can then call whichever control you like rather than setting a fixed value for the servo. For more information on controlling Qwiic devices, Sparkfun has several python examples, such as [this](https://learn.sparkfun.com/tutorials/qwiic-joystick-hookup-guide/all#python-examples).

We encourage you to try using these controls, **while** paying particular attention to how the interaction changes depending on the position of the controls. For example, if you have your servo rotating a screen (or a piece of cardboard) from one position to another, what changes about the interaction if the control is on the same side of the screen, or the opposite side of the screen? Trying and retrying different configurations generally helps reveal what a design choice changes about the interaction -- _make sure to document what you tried_!

### Part F
### Record

Document all the prototypes and iterations you have designed and worked on! Again, deliverables for this lab are writings, sketches, photos, and videos that show what your prototype:
* "Looks like": shows how the device should look, feel, sit, weigh, etc.


![IMG_6670](https://user-images.githubusercontent.com/42717070/138573801-d275849a-52d9-4ef6-8dcc-e1041104018f.jpg)

The device looks like a physical board game device with a eye-catching owl figure standing on it. With a cute figure and poppy colors, it gives a fun feeling while being educational. It has a box to contain the Pi and hide the sensor and wires that players don't need to see while still allows us to easily detach the Pi when needed by simply opening up the top. The box has ten alligator wires, five on each side, connecting to ten vocabulary cards. Cards on each side is colored diffrently so it's clear for the players to know which card belongs to whom, and the Pierre the Owl calculates the score and announces the winner by addressing the color as well. After acting it out ourselves, we found that asigning colors is more intuitive than using numeric identifier like player 1, 2.

It can be placed in any flat surfaces, ideally big enough to put all ten vocabulary cards and accomodate two players around it. We used an average-sized working desk to demonstrate. We designed both the box and cards light enough to be easily re-located for different occations. You can learn french on your dinner table, desk, on the carpet, or even at a park!

The box has three texts on it to guide the players: i)Title of the game ii) Score sign iii) how to start the game. Font size(big->small) and the layout(top->bottom) follows the importance of the information. We explored the layout of these informations before building the final design:
![IMG_6664](https://user-images.githubusercontent.com/42717070/138571542-ccf5c384-7b80-42d7-a438-1e13c21ea1f7.jpg)
![IMG_6665](https://user-images.githubusercontent.com/42717070/138571543-14d3cb24-40cc-4bcd-b200-bb5dbe14ff5a.jpg)

And printed out the texts to find the right size, iterated three times(ouch!) before we printed them on the colored paper:

![IMG_6666](https://user-images.githubusercontent.com/42717070/138571934-dc634d7b-23b0-47ff-9132-edeffc78c969.jpg)
![IMG_6667](https://user-images.githubusercontent.com/42717070/138571935-990586cd-8698-4c1c-b998-265594220edf.jpg)

![IMG_6668](https://user-images.githubusercontent.com/42717070/138573822-952f56ec-642a-4648-874f-83b50e6e7131.jpg)


* "Works like": shows what the device can do

Pierre the Owl is an interactive game device to learn basic French. It's a competition game between two players. Pierre speaks out loud a French vocabulary to teac and players will compete to find the corresponding English word faster. 

When the user presses any button to start(as instructed by the text on the box), Pierre the Owl, our beloved French teacher begin speaking. It introduces herself and explain the game rule:
> "Bonjour!
> "I am Pierre the owl and I am going to teach you french."
> "In this game, I will say a word in french and your task is to touch the corresponding word in english."
> "The player who touches the english card first will get the point"
> "If you want to hear the french word again, press any button"
> "Let's get started!"

We prepared five basic vocabulraries to learn, regarding food(I mean, what else): Wine, Chocolate, Cheese, Bread, Water
Pierre speaks in French, players either touch the corresponding card or press the button to listen to replay the word, Pierre keeps the score and display it on the screen, repeat for five rounds. 
At last, the final winner is announced verbally. 
![IMG_6671](https://user-images.githubusercontent.com/42717070/138573805-b4524184-64c2-4ad1-bf3f-e956e061f43a.jpg)



* "Acts like": shows how a person would interact with the device



https://user-images.githubusercontent.com/42717070/138573814-7f809f69-7de2-459a-a101-0d10cfbe764b.mov



Players will find this device placed on a desk. Walk up to it, read the texts on the box, find out it's a device to learn French and presse the button to start if interested. After listening to Pierre's verbal instructions, players will touch the card that they think is the answer. If the players wish to listen to the French word again, he/she can press any of the buttons.



