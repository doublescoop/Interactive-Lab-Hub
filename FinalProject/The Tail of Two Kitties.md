# The Tail of Two Kitties
![IMG_8419](https://user-images.githubusercontent.com/42717070/145831662-873f7104-8b06-40e4-8433-74732a62bf93.jpg)


#### The cat evolution in one pic: 
![IMG_8383](https://user-images.githubusercontent.com/42717070/145831501-6b945932-9fab-43d0-b0a9-889750d2782a.jpg)

## Project Description
This project consists of two interactive kitties that respond in cat like ways when touched by the user. When pet the cats purr, wag thier tags, move thier paws, and meow. These two cats are also connected via MQTT. When both cats are being interacted with at the same time their hearts warms up(light on!),and the cats will meow in joy. The goals of this project are to create an emotional experience for users similar to petting a cat and to connect long distance friends through interacting with our cats.
The inspiration for this project stems a lot from our time quarantined during 2020 and wishing we had both a pet to interact with and connection with our friends. We were also very much inspirated by the research of Ran Zhou that highlights the emotional response in users from robotic physical contact (https://www.ranzhourobot.com/).

[add story board]


## Design Process
To create these two cats we used the following technology:
- Raspberry Pi
- Capacitive touch sensors
- Servo motors
- MQTT communication
- Speakers
- LED Light
The appearance of the cats was made up of:
- Cardboard
- A furry sweater
- Conductive tape
- Wire
- Yarn
- Ribbon
- Redbull cans 

### Prototype in 2D
![Untitled_Artwork](https://user-images.githubusercontent.com/42717070/145827982-43133f51-25ad-4d52-be62-b954cda9e619.jpg)

To start building these two cats, we first created a simple 2D card borad verison of the cats to ensure all the technology would work well together and to prototype user ineraction. The 2D verison of the cats used the servo motor to move a cardbord arm of the cat when it is touched. The 2D cats also purr when they are touched and demonstrate the connection between the two cats when both 2D cats are touched at the same time by shine a red LED light through a paper heart. 
#### design considerations in 2D prototyping of the kitties:
[Appearance] 
- What is the overall look and feel we want? Why? : Cute and soft. Our goal is to arouse 'AWW I WANT TO TOUCH YOU' reaction from the user. We want to recreate the soothing and joyful experience with a cat, not a scary one.,
- Shape and posture: standing? seating? : Seated, because it gives more stability in the shape and we imagined it to be more natural for cat to move her arm while seated. 
- Realistic facial features or cartoonish? : Cartoonish, it might look scary or creepy with a realistic features. We drew few realistic eyes and knew right away it is going to scare people. 
- Locations for the tail, arm, and heart? : Locations of the moving body parts had to be realistically adopting its positions in the real cat but also feasible for us to build with the sensors. From the prototyping, we learned that users tend to be forgiving towards slightly unnatural positions of body parts. 
- Locations for the sensors and wires? : We hid the pi, sensors, speaker, and wires all behind the cardbox. It was easy for a quick 2D prototyping but through this process we realised the cat's body will have to leave some hollow space for the sensors for 3D.
- We discussed the look and feel of the kitties as well, but it did not really matter for the 2D prototyping. We focused on the functionality check. 


[Functions]
- How should we initiate the interaction? We considred face recognition (when human stares at the cat from the front) or body recognition (when waving at the cat) or proximity (when near by) or captive (when touched). We decided to go for the touch first and build the wave recognition part if time allows. We dropped the face recognition and proximity because we imagined it will be hard to control the background at the showcase(open studio). 
- What should happen, when, and why? HUMAN TOUCH -> HAPPY CAT -> TOUCHES BACK is our main flow for the interaction. When human touches the cat, the cat will purr, wag her tail, or meow to indicate that she's feeling the touch and happy about it. The cat can also move her arm in attempt to touch the person back. 
- Which parts should be touched? We tested with random students at Tata to see where do they naturally want to touch a cat. Mostly back, paw and sometimes the face. From this, we decided to put most of our sensors on the back. 



[Perhaps talk more about how the tech of the cats works] @Jay

Appearance of the two cats:
<img width="975" alt="Screen Shot 2021-12-12 at 10 27 58 PM" src="https://user-images.githubusercontent.com/73661058/145747859-02a0b7d6-1545-4ae9-8d12-89e53d377581.png">

One cat working:
https://user-images.githubusercontent.com/73661058/145748293-b33c4179-f564-44e3-8904-8b506f14eace.mov

Two cats working together:
https://user-images.githubusercontent.com/42717070/145828042-17c11f66-937c-43e8-b876-2cd13c1d8046.mov

Back view of the cats:

<img width="546" alt="Screen Shot 2021-12-12 at 10 29 19 PM" src="https://user-images.githubusercontent.com/73661058/145747959-8223169d-07ca-407b-9071-c8cad17d4071.png">


### 2D to 3D 

After validating that all of our technological components worked well together and testing our 2D cats with some peer users we began constructing the 3D cats. 
Our plan to create these 3D cats was to created a cardborad skeleton for the cats, place wires for sensors and servo motors in the skelton and cover the cardboard skelton with fur to give a cat like appearance and feel.

#### [Apperance_ Look and Feel, outer shell]

![IMG_3095](https://user-images.githubusercontent.com/42717070/145834958-7f998966-c668-440f-bae7-3620ca3dcc71.jpg)

The spectrum of cat's image is very wide. It can be a creepy scary cat or the cuteset thing ever. We wanted to make sure our kitties gives a soft, warm, and cute look. Because we intend to give users a soothing and joyful experience with connected cat, something they want to touch when they miss friends or feeling lonely, not to be scared with it. 

So we decided to give the cat a fluffy fur outer shell. We went to a GoodWill in UES. Found a fur sweater $7! More details below for the process of tailoring.

![IMG_3099](https://user-images.githubusercontent.com/42717070/145835388-9e21ce18-d6ba-4844-b9fa-bf71eb66b09e.jpg)


#### [Appearance_ shape and structure]

To create the cats cardbord skelton, we found some 3D model puzzles online and used to a laser cutter to cut them pieces. This process took us much time and experimentations. The first cat 3D model puzzles we found looked nice but when cut there was way too many pieces and we struggled to put it together. We had to give up on finding a seated shape of the cat.
This lead us to finding a new model with less pieces that was more managable for our project. Once we selected our model we had to experiment with cardboard thickness to find the best possible skeltons for our kitties. 

Complicated cat 3D model puzzle that we failed to use:

<img width="548" alt="Screen Shot 2021-12-12 at 10 56 34 PM" src="https://user-images.githubusercontent.com/73661058/145750070-ba868da3-1f17-4aed-983a-bf56a8d5b873.png">

Simpler cat 3D model puzzle we used:

![IMG_7064](https://user-images.githubusercontent.com/73661058/145750078-69435904-f33b-41a9-aba5-3f87c68b9e88.jpg)
Since the models we found online didn't have the right scale(size) that we wanted, we had to re scale the stl file. In this process, the gap left for puzzling in cardboxes got proportionally bigger as well which did not work with the thin cardboxes we had. But at last, having these gaps turned out to be useful to allow more space for servo motor and wires. (There was a lot of glueing job, though) 

#### [Function_ Movements with servo motor!]


Once had our cardboard skeletons created, we added in the servo motors and tested out the movement of our kitties as skelton cats. To do this, we detached the arm of the cat, cut a gap in the skelton to place the motor, and hot glued the detached cat arm to the wing of the motor. For the tail, we started by completely removing the cardboard tail and replacing it with wire cover in yarn (a more realistic looking tail). then the cut another gap in the rear of the cats to place thier tail motors.
![IMG_8357](https://user-images.githubusercontent.com/42717070/145837526-1953e7bb-18a4-4665-a740-97e81d3380b9.jpg)
![IMG_8333](https://user-images.githubusercontent.com/42717070/145839565-64e6bc63-8586-413f-96ee-c61f93fc9b2e.jpg)


[Add any details I am missing here and any additional photos you have]

Photos of this stage:
<img width="829" alt="Screen Shot 2021-12-12 at 11 09 28 PM" src="https://user-images.githubusercontent.com/73661058/145751091-66acae65-2b39-4e8b-8f7c-f1fc218a6c93.png">
<img width="556" alt="Screen Shot 2021-12-12 at 11 09 58 PM" src="https://user-images.githubusercontent.com/73661058/145751120-eb435b79-7ca3-4506-8318-b09975b34ad5.png">
![IMG_8330](https://user-images.githubusercontent.com/42717070/145839575-9ac0832f-a893-439b-a085-ab8c7ef84199.jpg)
we also cut out the moving parts at this stage, experiemented with the range of the movements with a thinner paper. 
Since we used a 3D puzzle for the skeleton, it had multiple layers. It was important to mark the precise position of the servo motor through out all the layers so it doesn't affect the movement or the shape. 



#### [Function_ Touch detection with capacitive sensors]

Next we add metal places to the skelton for touch sensors [discuss how and why this failed] attached to alligator clips and covered the skeltons in furr. 


#### [Appearance_ Final clothing]

With the old sweater we thirfted from Good Will, we clothed the kitties at last. 
To get a cat shape from the fur fabric we first created a pattern with another thinner fabric and then cut it out of the thick fur material. 
Lastly we hot glued the furr coat on to the cat skeltons.

Fabric pattern for furr:
<img width="542" alt="Screen Shot 2021-12-12 at 11 31 00 PM" src="https://user-images.githubusercontent.com/73661058/145752752-78581013-b9c8-45e8-9572-f4337c93e5a9.png">
<img width="551" alt="Screen Shot 2021-12-12 at 11 31 39 PM" src="https://user-images.githubusercontent.com/73661058/145752815-ab649266-ac61-4278-8fc2-e5c512987300.png">
<img width="553" alt="Screen Shot 2021-12-12 at 11 32 16 PM" src="https://user-images.githubusercontent.com/73661058/145752843-591fb3e4-3495-4e68-9346-fa541159cbaf.png">
Cat covered in furr:
<img width="529" alt="Screen Shot 2021-12-12 at 11 32 57 PM" src="https://user-images.githubusercontent.com/73661058/145752889-6070a3bf-a233-4c88-8f0a-3ef64048f2d8.png">
[Add more details here and any more photos you have]


#### [Function_ Warm up the heart! ]

The last step to the cats appearance was to add the heart light for interaction between the two cats. To do this we taped the LED lights to the chest of the cats, covered them in a thin furr to intensify thier shine, and put a duct tape heart on top of the chest furr.

Heart light:

<img width="509" alt="Screen Shot 2021-12-12 at 11 33 32 PM" src="https://user-images.githubusercontent.com/73661058/145752955-b879156c-d9de-4477-85e1-e24a95d62769.png">

![IMG_8363](https://user-images.githubusercontent.com/42717070/145840052-d333aa12-4eed-4dcf-9a43-bc69f551ab88.jpg)

Because of the standing shape of the cat, the heart had to be positioned down in the chest. 
Since we designed this kitty to be placed on a table and the user will be highly likely interacting in a standing position, the visibility of the heart light from the user was problematic. 
So we experimented with different material (A yarn we found in the MakerLab) to amplify the lighting with diffusing effect. 

![IMG_8363](https://user-images.githubusercontent.com/42717070/145840486-d9c72f7d-42dc-4108-8a04-8b98189278bf.jpg)

We kept the yarn for the entire chest but used a cutout sticker to emphasize the heart shape for our final design. 



#### [Appearnce_Box to hide the machinaries]
Under the cats we added a box for cat to stand on. This served to stablize the cat allowing it to stand and hide the pi, senors, and speaker from the user.
[Discuss more about the cats stand and box if necessary]
[In general add any photos or details I missed from this section]


## Final Device Design
Final look:
<img width="528" alt="Screen Shot 2021-12-12 at 11 39 15 PM" src="https://user-images.githubusercontent.com/73661058/145753356-41e7d3c1-1dbd-4fe7-8f7a-37ed99b667da.png">
Evolution of the cats:
<img width="987" alt="Screen Shot 2021-12-12 at 11 40 52 PM" src="https://user-images.githubusercontent.com/73661058/145753486-5a504150-8990-4678-a394-a148412aaba7.png">
Cats working:
https://user-images.githubusercontent.com/73661058/145753313-f118803b-0259-4138-ba82-10a24565e6ff.mov
Us with the cats :blush: :
<img width="517" alt="Screen Shot 2021-12-12 at 11 40 29 PM" src="https://user-images.githubusercontent.com/73661058/145753457-aa2a2e7b-e35a-41ef-ba3f-67a6326bb5cb.png">
[Add any more photos for photos and videos]
[any comments about peoples reactions and interacts with the cats ]


## Showtime!

- Meeting humans at the IDD class:

https://user-images.githubusercontent.com/42717070/145840834-05af1ffe-5cc3-4e0d-8301-7d49253344c6.MOV

- Purring at the Open Studio: 
![IMG_8448](https://user-images.githubusercontent.com/42717070/145841007-07cc3c51-e4b5-4dd9-8efa-295c5c7562e0.jpg)


https://user-images.githubusercontent.com/42717070/145842269-49b2aa1d-128c-4981-b328-73069f37d2a7.MOV



This women in the video was keep patting our kitty with full firmness and towards the end of the tail as if she's touching her own, real, cat. 
It was thrilling to see some people interacting with the robot kitties in the same way they'd touch a real cat. 

-
Other best comments from the users we met at the Open Studio:
"I'm alergic to cat. OMG I NOW CAN TOUCH THE CAT"
"This is addictive(still patting)"
"Can I buy this?"


