# The Tail of Two Kitties
- Interactive Robot-cats Meeting Humans:
  
https://user-images.githubusercontent.com/42717070/145901099-ba9b7939-6443-43dd-87de-74a6f8c827c9.mov


## What is this project?

This project consists of two interactive kitties that respond in cat-like ways when touched by the user. When interacted with through petting, the cats purr, wag their tails, move their paws, and meow. These two cats are also connected. When both cats are being interacted with at the same time a heart light will turn on, on both the cats and the cats will meow. The goals of this project are to create an emotional experience for users similar to petting a cat and to connect long distance friends through interacting with our cats.

The inspiration for this project comes from our feelings and the feelings of the people surrounding us during the pandemic. During this time and especially during quarantine, we saw that people were feeling trapped in their homes with nothing to do and, more importantly, isolated from people they care about. In response to this, a lot of people decided to get dogs, cats, or other pets to try to fill that void, but there are two problems with this. The first is that not everyone is able to get a pet due to cost, allergies, or other reasons, and the second is that this does not change the fact that people have been separated from their loved ones. We wanted to try and fix these problems with robotic pets that are individually interactive, but that are also connected so that people that are geographically separated can be connected in a way that feels organic. 

We were also very much inspired by the research of Ran Zhou that highlights an emotional response in users from robotic physical contact (https://www.ranzhourobot.com/).

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

### Design Considerations

Appearance

- Overall look and feel: Cute and soft. Our goal is to cause a pemotional reaction from the user. We want to recreate the soothing and joyful experience with a cat, not a scary one.,
- Shape and posture: Seated, because it gives more stability in the shape and we imagined it to be more natural for cat to move her arm while seated.
- Realistic or cartoonish: Cartoonish, it might look scary or creepy with a realistic features. We drew few realistic eyes and knew right away it is going to scare people.
- Locations for the tail, arm, and heart: Locations of the moving body parts had to be realistically adopting its positions in the real cat but also feasible for us to build with the sensors. From the prototyping, we learned that users tend to be forgiving towards slightly unnatural positions of body parts.
- Locations for the sensors and wires: We hid the pi, sensors, speaker, and wires all behind the cardbox. It was easy for a quick 2D prototyping but through this process we realised the cat's body will have to leave some hollow space for the sensors for 3D.
- We discussed the look and feel of the kitties as well, but it did not really matter for the 2D prototyping. We focused on the functionality check.


Functions

- Initiating interaction: We considred face recognition (when human stares at the cat from the front) or body recognition (when waving at the cat) or proximity (when near by) or captive (when touched). We decided to go for the touch first and build the wave recognition part if time allows. We dropped the face recognition and proximity because we imagined it will be hard to control the background at the showcase (open studio).
- Interaction flow: HUMAN TOUCH -> HAPPY CAT -> TOUCHES BACK is our main flow for the interaction. When human touches the cat, the cat will purr, wag her tail, or meow to indicate that she's feeling the touch and happy about it. The cat can also move her arm in attempt to touch the person back.
- Locations of touch sensors: We tested with random students at Tata to see where do they naturally want to touch a cat. Mostly back, paw and sometimes the face. From this, we decided to put most of our sensors on the back.

### Prototype in 2D

![Untitled_Artwork](https://user-images.githubusercontent.com/42717070/145827982-43133f51-25ad-4d52-be62-b954cda9e619.jpg)

To start building these two cats, we first created a simple 2D cardboard verison of the cats to test the technology would work well together and to prototype user interaction. The 2D verison of the cats used the servo motor to move a cardboard arm of the cat when it is touched. The 2D cats also purr when they are touched, and they show the connection between the two cats by shining a red LED light through a paper heart when both are interacted with at the same time.

Appearance of the two cats:

<img width="975" alt="Screen Shot 2021-12-12 at 10 27 58 PM" src="https://user-images.githubusercontent.com/73661058/145747859-02a0b7d6-1545-4ae9-8d12-89e53d377581.png">

One cat working:

https://user-images.githubusercontent.com/73661058/145748293-b33c4179-f564-44e3-8904-8b506f14eace.mov

Two cats working together:





https://user-images.githubusercontent.com/42717070/145901068-b5ad8bc8-5039-4bbf-99db-e8984b885482.mov



Back view of the cats:

<img width="546" alt="Screen Shot 2021-12-12 at 10 29 19 PM" src="https://user-images.githubusercontent.com/73661058/145747959-8223169d-07ca-407b-9071-c8cad17d4071.png">

To make this technology work, we had to integrate several different functions into the program because a making something "interactive" almost by definition means there must be more than one type of action from the user to start an interaction and more than one type of reaction from the device in response. For each individual cat, we used capacitive sensors, speakers, servo motors, and MQTT communication. Here is a diagram of the full system architecture:

![image](https://user-images.githubusercontent.com/67603876/145860922-fc8fa2b2-c298-4d65-b751-c4fdadccd171.png)

The interactions alone have all individually been done before in previous labs, so integrating them was the biggest technological challenge. Since there were so many things connected and running at the same time, it was easy for us to miss something being slightly unplugged or for the Raspberry Pi to miss when one of the sensors was touched, so we ran into a lot of Remote I/O errors while prototyping. Additionally, the connection to the MQTT server would drop on occasion, which we mainly worked around by restarting the program, and this seemed to work.

As seen in the above images, the capacitive touch sensors were connected by alligator clips to rectangular conductive strips that we made by cutting up a soda can, which we thought would be ideal because they are thin and light, while also being easy to clip onto and tape down, as well as being conductive. We would use this same method of spreading out the touchable areas of the sensors in the final design of the cat, until we ran into some problems, which will be discussed later. Regardless, these "touch pads" worked well for the prototype, and the other functions did not cause many issues.

### 2D to 3D

After validating that all of our technological components worked well together and testing the interactions of our 2D cats with some peer users we began constructing the 3D cats. Our plan to create these 3D cats was to created a cardboard skeleton for the cats, place wires for sensors and servo motors in the skelton and cover the cardboard skelton with fur to give a cat like appearance and feel. In our user testing, we found that people loved the idea of the interactive robotic pet, but the unrealistic look of the 2D prototype was certainly a factor in making the experience more artificial than it should be. For this reason, we knew we had to really create a realistic-enough looking 3D cat and find a way to integrate our technology into it; otherwise, our final product would not have the desired effect of bringing people comfort.

#### Appearance / Look and Feel

![IMG_3095](https://user-images.githubusercontent.com/42717070/145834958-7f998966-c668-440f-bae7-3620ca3dcc71.jpg)

The spectrum of the perception of a cat based on looks is quite large, ranging from ominous and creepy to comforting and cute. We want to give users a soothing and joyful experience with connected cat, something they want to touch when they miss friends or feeling lonely, not to be scared with it.

So we decided to give the cat a fluffy fur outer shell. We went to a GoodWill in the Upper East Side and found a fur sweater for only $7. The way we tailored this sweater is discussed later.

![IMG_3099](https://user-images.githubusercontent.com/42717070/145835388-9e21ce18-d6ba-4844-b9fa-bf71eb66b09e.jpg)

#### Appearance / Shape and Structure

To create the cats cardboard skelton, we found some 3D model puzzles online and used to a laser cutter to cut them pieces. This process took us much time and experimentation. The first cat 3D model puzzles we found looked nice but when cut there were  too many pieces, and we struggled to put it together. This led us to look for a new model with less pieces that was more manageable for our project. Once we selected our model, we had to experiment with cardboard thickness to find the best possible skeletons for our kitties.

Over-complicated cat 3D model puzzle:

<img width="548" alt="Screen Shot 2021-12-12 at 10 56 34 PM" src="https://user-images.githubusercontent.com/73661058/145750070-ba868da3-1f17-4aed-983a-bf56a8d5b873.png">

Simpler cat 3D model puzzle we used:

![IMG_7064](https://user-images.githubusercontent.com/73661058/145750078-69435904-f33b-41a9-aba5-3f87c68b9e88.jpg)

Since the models we found online didn't have the right scale that we wanted, we had to rescale the .stl file. In this process, the gap left for fitting pieces in got proportionally bigger, which we first thought did not work with the thin cardboard pieces we had. However, having these larger gaps turned out to be useful in the end to allow more space for servo motor and wires. We just had to add more glue than was expected to fill in the gaps and make sure the structure was stable.

#### Function / Movements with the servo motors

Once we had our cardboard skeletons created, we added in the servo motors and tested out the movement of our kitties as skelton cats. Our design is built around a few central frame pieces, so to get our servos to be in the right spots, we had to attach them to one of those central pieces. This was done easily with tape (instead of glue to avoid complications of glue directly on electronics), but the motors are slightly too large to fit between two central pieces in our puzzle piece model. To fix this, we cut holes in the next piece over so that the motors would just fit through them without messing up the structural integrity of the cat. There were two servo motors per cat that had to be attached, one at the arm and one at the tail. 

As seen in the image directly above, the edge piece of the cardboard model includes both left legs in one piece (we call the front leg the "arm" for simplicity's sake). Consequently, we first detached the arm of the cat from that edge piece of the model so that it could be moved separately from the left leg, the concept and initial testing aspects of this shown in this image:

![IMG_8330](https://user-images.githubusercontent.com/42717070/145839575-9ac0832f-a893-439b-a085-ab8c7ef84199.jpg)

As shown, we experiemented with the range of the movements with a thinner paper. Since we used a 3D puzzle for the skeleton, it had multiple layers. It was important to mark the precise position of the servo motor throughout all the layers so that we can make sure the movement of the arm does not hit the cat's face and prevent similar issues.

We then cut a gap in the skeleton as mentioned above to place the motor. We also had to cut a small hole in the original piece that held the arm because just the small part of the motor that holds the moving attachment had to poke through. Lastly, we hot glued the detached cat arm to the attachment of the motor, so that the arm can move on its own outside the stationary frame, giving the illusion of a shoulder joint. For the tail's motor, we started by completely removing the cardboard tail that was part of the original model, and we replaced it with a more realistic looking tail, which consisted of yarn wrapped around a wire to hold its shape. Then, we placed the motor in a similar way to the arm motor, and that was enough for the tail to work. The taped servo motor and the tail on the central piece of cardboard is shown here:

![IMG_8333](https://user-images.githubusercontent.com/42717070/145839565-64e6bc63-8586-413f-96ee-c61f93fc9b2e.jpg)

Photos of this stage:

<img width="829" alt="Screen Shot 2021-12-12 at 11 09 28 PM" src="https://user-images.githubusercontent.com/73661058/145751091-66acae65-2b39-4e8b-8f7c-f1fc218a6c93.png">
<img width="556" alt="Screen Shot 2021-12-12 at 11 09 58 PM" src="https://user-images.githubusercontent.com/73661058/145751120-eb435b79-7ca3-4506-8318-b09975b34ad5.png">

#### Function / Capacitive touch sensors

Next we added the same conductive strips that were used in the 2D model to the 3D skeleton for the touch sensors, which we attached to alligator clips that ran through the skeleton out the bottom. Before doing this, we did some testing with these strips because our plan was to put these sensors underneath the fur of the cat because they are capacitive, so we thought they may work. To test this, we just tried putting different types of materials, as well as the fur we chose (details discussed later) on top of the strips and seeing if we could just sense a touch. During our testing, this seemed to work with no problems, so after we were convinced that it would work, we went through with the plan. Here is what this looked like:

![image](https://user-images.githubusercontent.com/67603876/145869865-0fa5d3b0-c548-41f0-b22c-aa4f1e56e9e9.png)

#### Appearance / Fur and outer shell

The next step was to cover the skeletons in some type of "fur" so that the cat would feel nice to pet. For the cat fur we used the old sweater we thrifted from GoodWill as mentioned above. To get a cat shape from the fur, we first created a pattern with thinner fabric by testing out different shapes and wrapping methods on the skeleton, and once we found the best shape, we cut it out of our fur-like material (the sweater). Lastly, we hot glued the fur coat on to the cat skeltons.

Fabric pattern for fur:

<img width="542" alt="Screen Shot 2021-12-12 at 11 31 00 PM" src="https://user-images.githubusercontent.com/73661058/145752752-78581013-b9c8-45e8-9572-f4337c93e5a9.png">
<img width="551" alt="Screen Shot 2021-12-12 at 11 31 39 PM" src="https://user-images.githubusercontent.com/73661058/145752815-ab649266-ac61-4278-8fc2-e5c512987300.png">
<img width="553" alt="Screen Shot 2021-12-12 at 11 32 16 PM" src="https://user-images.githubusercontent.com/73661058/145752843-591fb3e4-3495-4e68-9346-fa541159cbaf.png">

Cat covered in fur:

<img width="529" alt="Screen Shot 2021-12-12 at 11 32 57 PM" src="https://user-images.githubusercontent.com/73661058/145752889-6070a3bf-a233-4c88-8f0a-3ef64048f2d8.png">

After putting the fur on, we decided to test that the sensors worked one more time. It did work at first after the fur was put on and glued down, but at some point, the touch sensors completely stopped working under the fur, and the only way to trigger them after this point was by either poking through the fur with a conductive needle, or reaching underneath the fur to touch the strips directly. We speculated that having the fur taut and attached onto the sensors for an extended period of time meant the touch sensors may always be activated for some reason, so any further activation by touching the fur would not cause any change in sensor output. Another possible reason is that the fur and the strips had some long-term interaction electrically, which may have brought the fur to a point were any touch would not change its electromagnetic structure enough to change what the sensor detects. In any case, we experimented with cutting holes in the fur (which did not work reliably), having small conductive bumps that connected directly to the strips (which ruined the realistic and comforting sensation when petting the cats), and a few other attempts to fix this. We finally settled on instead wrapping one conductive tape strip around the furr, which were placed where the user is most likely to touch them while petting the intended areas of the cat, and connecting those directly to the touch sensors. These brass-colored strips can be seen in the final images of the working cats. This design worked out quite well, as there were rarely any times where the user was unable to hit the right spots to cause an interaction with the cat.

#### Function / Warm up the heart

The last step to the cats appearance was to add the heart light for interaction between the two cats. To do this we taped the LED lights to the chest of the cats, covered them in a thin cotton-like fur to spread the light to a shape and size we wanted, and duct taped a heart on top of the chest furr.

Heart light:

<img width="509" alt="Screen Shot 2021-12-12 at 11 33 32 PM" src="https://user-images.githubusercontent.com/73661058/145752955-b879156c-d9de-4477-85e1-e24a95d62769.png">

Because of the standing shape of the cat, the heart had to be positioned down in the chest. Since we designed it to be placed on a table and the user will likely be interacting with it while standing, the visibility of the heart light from the user was problematic. To solve this issue, we experimented with different material (A yarn we found in the MakerLab) to amplify the lighting with diffusing effect.

![IMG_8363](https://user-images.githubusercontent.com/42717070/145840052-d333aa12-4eed-4dcf-9a43-bc69f551ab88.jpg)

We kept the yarn for the entire chest but used a cutout sticker to emphasize the heart shape for our final design.

#### Appearance / Pedestal for the cats and electronics

Under the cats, we added a pedestal for cat to stand on. This served to stablize the cat, allowing it to stand, as well as hide the Raspberry Pi, senors, speaker, and other electronics from the user. We re-used a box we found in a recycling bin, and cut it to do exactly what we needed. Specifically, we needed the box to have one side open faced, so that wires like the power chord can come out of it and so that we can reach in to fix or adjust anything if needed. We also needed small holes on top of the pedestal so that wires that run through the bottom of the cat skeleton can come through the box and connect to the electronics within the box. In order to do this in the most elegant way, we taped all the wires that run through the cat to either of the right legs of the cat and cut the holes in the box to be right next to those legs. This allowed us to hide the wires from the user, which is a major part of creating that realistic experience. We made two of these pedestals by cutting the recycled box in half, cutting the holes we needed by precisely measuring their sizes and positions, and cutting a separate piece of cardboard to make the sides that were left open by cutting the original box in half. We then cut some tablecloth-like fabric to go over the box for aesthetic purposes, which can also be seen in the final images of the working cats.


## Final Device Design

Final look:

<img width="528" alt="Screen Shot 2021-12-12 at 11 39 15 PM" src="https://user-images.githubusercontent.com/73661058/145753356-41e7d3c1-1dbd-4fe7-8f7a-37ed99b667da.png">

Evolution of the cats:

<img width="987" alt="Screen Shot 2021-12-12 at 11 40 52 PM" src="https://user-images.githubusercontent.com/73661058/145753486-5a504150-8990-4678-a394-a148412aaba7.png">

Cats working:

https://user-images.githubusercontent.com/73661058/145753313-f118803b-0259-4138-ba82-10a24565e6ff.mov

Us with the cats :blush: :

<img width="517" alt="Screen Shot 2021-12-12 at 11 40 29 PM" src="https://user-images.githubusercontent.com/73661058/145753457-aa2a2e7b-e35a-41ef-ba3f-67a6326bb5cb.png">

## Showtime!


- Purring at the Open Studio:
![IMG_8448](https://user-images.githubusercontent.com/42717070/145841007-07cc3c51-e4b5-4dd9-8efa-295c5c7562e0.jpg)

https://user-images.githubusercontent.com/42717070/145842269-49b2aa1d-128c-4981-b328-73069f37d2a7.MOV

This person in the video above was petting the cat very firmly and stroking its back all the way through the end of the tail, which is how many people pet a real cat. It was as if she was touching her own cat at home. It was thrilling to see some people interacting with our robot cats in the same way they would with a real one and seeing their reactions to how our cats interacted with them.


Other best comments from the users we met at the Open Studio:

- "I'm alergic to cats. OMG NOW I CAN TOUCH THE CAT"
- "This is addictive"
- "Can I buy this?"
