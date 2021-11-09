# Observant Systems


For lab this week, we focus on creating interactive systems that can detect and respond to events or stimuli in the environment of the Pi, like the Boat Detector we mentioned in lecture. 
Your **observant device** could, for example, count items, find objects, recognize an event or continuously monitor a room.

This lab will help you think through the design of observant systems, particularly corner cases that the algorithms needs to be aware of.

## Prep

1.  Pull the new Github Repo.
2.  Install VNC on your laptop if you have not yet done so. This lab will actually require you to run script on your Pi through VNC so that you can see the video stream. Please refer to the [prep for Lab 2](https://github.com/FAR-Lab/Interactive-Lab-Hub/blob/Fall2021/Lab%202/prep.md), we offered the instruction at the bottom.
3.  Read about [OpenCV](https://opencv.org/about/), [MediaPipe](https://mediapipe.dev/), and [TeachableMachines](https://teachablemachine.withgoogle.com/).
4.  Read Belloti, et al.'s [Making Sense of Sensing Systems: Five Questions for Designers and Researchers](https://www.cc.gatech.edu/~keith/pubs/chi2002-sensing.pdf).

### For the lab, you will need:

1. Raspberry Pi
1. Webcam 
1. Microphone (if you want to have speech or sound input for your design)

### Deliverables for this lab are:
1. Show pictures, videos of the "sense-making" algorithms you tried.
1. Show a video of how you embed one of these algorithms into your observant system.
1. Test, characterize your interactive device. Show faults in the detection and how the system handled it.

## Overview
Building upon the paper-airplane metaphor (we're understanding the material of machine learning for design), here are the four sections of the lab activity:

A) [Play](#part-a)

B) [Fold](#part-b)

C) [Flight test](#part-c)

D) [Reflect](#part-d)

---

### Part A
### Play with different sense-making algorithms.

#### OpenCV
A more traditional method to extract information out of images is provided with OpenCV. The RPI image provided to you comes with an optimized installation that can be accessed through python. We included 4 standard OpenCV examples: contour(blob) detection, face detection with the ``Haarcascade``, flow detection (a type of keypoint tracking), and standard object detection with the [Yolo](https://pjreddie.com/darknet/yolo/) darknet.

Most examples can be run with a screen (e.g. VNC or ssh -X or with an HDMI monitor), or with just the terminal. The examples are separated out into different folders. Each folder contains a ```HowToUse.md``` file, which explains how to run the python example. 

Following is a nicer way you can run and see the flow of the `openCV-examples` we have included in your Pi. Instead of `ls`, the command we will be using here is `tree`. [Tree](http://mama.indstate.edu/users/ice/tree/) is a recursive directory colored listing command that produces a depth indented listing of files. Install `tree` first and `cd` to the `openCV-examples` folder and run the command:

```shell
pi@ixe00:~ $ sudo apt install tree
...
pi@ixe00:~ $ cd openCV-examples
pi@ixe00:~/openCV-examples $ tree -l
.
├── contours-detection
│   ├── contours.py
│   └── HowToUse.md
├── data
│   ├── slow_traffic_small.mp4
│   └── test.jpg
├── face-detection
│   ├── face-detection.py
│   ├── faces_detected.jpg
│   ├── haarcascade_eye_tree_eyeglasses.xml
│   ├── haarcascade_eye.xml
│   ├── haarcascade_frontalface_alt.xml
│   ├── haarcascade_frontalface_default.xml
│   └── HowToUse.md
├── flow-detection
│   ├── flow.png
│   ├── HowToUse.md
│   └── optical_flow.py
└── object-detection
    ├── detected_out.jpg
    ├── detect.py
    ├── frozen_inference_graph.pb
    ├── HowToUse.md
    └── ssd_mobilenet_v2_coco_2018_03_29.pbtxt
```

The flow detection might seem random, but consider [this recent research](https://cseweb.ucsd.edu/~lriek/papers/taylor-icra-2021.pdf) that uses optical flow to determine busy-ness in hospital settings to facilitate robot navigation. Note the velocity parameter on page 3 and the mentions of optical flow.

Now, connect your webcam to your Pi and use **VNC to access to your Pi** and open the terminal. Use the following command lines to try each of the examples we provided:
(***it will not work if you use ssh from your laptop***)

```
pi@ixe00:~$ cd ~/openCV-examples/contours-detection
pi@ixe00:~/openCV-examples/contours-detection $ python contours.py
...
pi@ixe00:~$ cd ~/openCV-examples/face-detection
pi@ixe00:~/openCV-examples/face-detection $ python face-detection.py
...
pi@ixe00:~$ cd ~/openCV-examples/flow-detection
pi@ixe00:~/openCV-examples/flow-detection $ python optical_flow.py 0 window
...
pi@ixe00:~$ cd ~/openCV-examples/object-detection
pi@ixe00:~/openCV-examples/object-detection $ python detect.py
```

**\*\*\*Try each of the following four examples in the `openCV-examples`, include screenshots of your use and write about one design for each example that might work based on the individual benefits to each algorithm.\*\*\***

<img width="356" alt="Screen Shot 2021-11-02 at 12 32 43 AM" src="https://user-images.githubusercontent.com/42717070/139787655-24ad59c3-9ec4-4608-a086-15a4a97413cf.png">
- object detection: could be used in detecting if someone has a full equipment set ready before starting some DIY projects/cooking/any project that require a set of objects ready.


<img width="381" alt="Screen Shot 2021-11-02 at 12 19 15 AM" src="https://user-images.githubusercontent.com/42717070/139787657-e5002063-ff9c-4586-90db-edd80dcb2339.png">
- Face recognition: could be used in detecting whether someone is wearing a mask or not when entering an indoor space during pandemic.


<img width="373" alt="Screen Shot 2021-11-02 at 12 39 28 AM" src="https://user-images.githubusercontent.com/42717070/139787828-fbc84e10-cb29-4d1f-860c-706be215946e.png">
- flow detection: could be used in studying the workflow of physicians during treatments/surgery and improving the environment/interior accordingly.


<img width="348" alt="Screen Shot 2021-11-02 at 12 41 11 AM" src="https://user-images.githubusercontent.com/42717070/139787927-dd66a04d-c16a-41d8-ad26-889b4c89d806.png">
- contour detection: could be used in detecting shapes of organs and automating the annotation on top of a medical image. Or it could be used in detecting a logo and shape of a car and tell the maker and model of a car.  



#### MediaPipe

A more recent open source and efficient method of extracting information from video streams comes out of Google's [MediaPipe](https://mediapipe.dev/), which offers state of the art face, face mesh, hand pose, and body pose detection.

![Alt Text](mp.gif)

To get started, create a new virtual environment with special indication this time:

```
pi@ixe00:~ $ virtualenv mpipe --system-site-packages
pi@ixe00:~ $ source mpipe/bin/activate
(mpipe) pi@ixe00:~ $ 
```

and install the following.

```
...
(mpipe) pi@ixe00:~ $ sudo apt install ffmpeg python3-opencv
(mpipe) pi@ixe00:~ $ sudo apt install libxcb-shm0 libcdio-paranoia-dev libsdl2-2.0-0 libxv1  libtheora0 libva-drm2 libva-x11-2 libvdpau1 libharfbuzz0b libbluray2 libatlas-base-dev libhdf5-103 libgtk-3-0 libdc1394-22 libopenexr23
(mpipe) pi@ixe00:~ $ pip3 install mediapipe-rpi4 pyalsaaudio
```

Each of the installs will take a while, please be patient. After successfully installing mediapipe, connect your webcam to your Pi and use **VNC to access to your Pi**, open the terminal, and go to Lab 5 folder and run the hand pose detection script we provide:
(***it will not work if you use ssh from your laptop***)


```
(mpipe) pi@ixe00:~ $ cd Interactive-Lab-Hub/Lab\ 5
(mpipe) pi@ixe00:~ Interactive-Lab-Hub/Lab 5 $ python hand_pose.py
```

Try the two main features of this script: 1) pinching for percentage control, and 2) "[Quiet Coyote](https://www.youtube.com/watch?v=qsKlNVpY7zg)" for instant percentage setting. Notice how this example uses hardcoded positions and relates those positions with a desired set of events, in `hand_pose.py` lines 48-53. 
<img width="675" alt="Screen Shot 2021-11-02 at 12 58 07 AM" src="https://user-images.githubusercontent.com/42717070/139789320-1fab301a-8432-4f35-96db-c0c8e124386a.png">
<img width="340" alt="Screen Shot 2021-11-02 at 1 00 59 AM" src="https://user-images.githubusercontent.com/42717070/139789326-488f21ac-b5da-44e5-8a14-a52b8505a762.png">


**\*\*\*Consider how you might use this position based approach to create an interaction, and write how you might use it on either face, hand or body pose tracking.\*\*\***

It could be used as detecting a hand sign to signal the level of pain during a dentist visit. haha Usually they tell me to raise my left arm since I cannot speak while they're working on my mouth but it can only have binary extreme senario- YES pain and NO pain. Usually it's somewhere in between. Using the relative finger positions used in this system, we could detect four different levels of pain expressed by connecting one of the fingers to the thumb. 

(You might also consider how this notion of percentage control with hand tracking might be used in some of the physical UI you may have experimented with in the last lab, for instance in controlling a servo or rotary encoder.)



#### Teachable Machines
Google's [TeachableMachines](https://teachablemachine.withgoogle.com/train) might look very simple. However, its simplicity is very useful for experimenting with the capabilities of this technology.

![Alt Text](tm.gif)

To get started, create and activate a new virtual environment for this exercise with special indication:

```
pi@ixe00:~ $ virtualenv tmachine --system-site-packages
pi@ixe00:~ $ source tmachine/bin/activate
(tmachine) pi@ixe00:~ $ 
```

After activating the virtual environment, install the requisite TensorFlow libraries by running the following lines:
```
(tmachine) pi@ixe00:~ $ cd Interactive-Lab-Hub/Lab\ 5
(tmachine) pi@ixe00:~ Interactive-Lab-Hub/Lab 5 $ sudo chmod +x ./teachable_machines.sh
(tmachine) pi@ixe00:~ Interactive-Lab-Hub/Lab 5 $ ./teachable_machines.sh
``` 

This might take a while to get fully installed. After installation, connect your webcam to your Pi and use **VNC to access to your Pi**, open the terminal, and go to Lab 5 folder and run the example script:
(***it will not work if you use ssh from your laptop***)

```
(tmachine) pi@ixe00:~ Interactive-Lab-Hub/Lab 5 $ python tm_ppe_detection.py
```


(**Optionally**: You can train your own model, too. First, visit [TeachableMachines](https://teachablemachine.withgoogle.com/train), select Image Project and Standard model. Second, use the webcam on your computer to train a model. For each class try to have over 50 samples, and consider adding a background class where you have nothing in view so the model is trained to know that this is the background. Then create classes based on what you want the model to classify. Lastly, preview and iterate, or export your model as a 'Tensorflow' model, and select 'Keras'. You will find an '.h5' file and a 'labels.txt' file. These are included in this labs 'teachable_machines' folder, to make the PPE model you used earlier. You can make your own folder or replace these to make your own classifier.)

**\*\*\*Whether you make your own model or not, include screenshots of your use of Teachable Machines, and write how you might use this to create your own classifier. Include what different affordances this method brings, compared to the OpenCV or MediaPipe options.\*\*\***

<img width="929" alt="Screen Shot 2021-11-02 at 1 23 36 AM" src="https://user-images.githubusercontent.com/42717070/139794388-c37554e2-cd57-44a9-8feb-3058617f7ac9.png">
<img width="1085" alt="Screen Shot 2021-11-02 at 1 33 08 AM" src="https://user-images.githubusercontent.com/42717070/139794390-2eba20e7-2dc5-4042-af84-efcea5c1a8bf.png">
I was not sure if the detection from teachable model was performing well from the given code, as it was detecting my cup, phone, and hand all as 'mask'. However, it did perform very well when I trained my own images. I trained four classes: me holding a blue piece of paper, red piece of paer, empty background, and me holding nothing(face). 


*Don't forget to run ```deactivate``` to end the Teachable Machines demo, and to reactivate with ```source tmachine/bin/activate``` when you want to use it again.*


#### Filtering, FFTs, and Time Series data. (optional)
Additional filtering and analysis can be done on the sensors that were provided in the kit. For example, running a Fast Fourier Transform over the IMU data stream could create a simple activity classifier between walking, running, and standing.

Using the accelerometer, try the following:

**1. Set up threshold detection** Can you identify when a signal goes above certain fixed values?

**2. Set up averaging** Can you average your signal in N-sample blocks? N-sample running average?

**3. Set up peak detection** Can you identify when your signal reaches a peak and then goes down?

**\*\*\*Include links to your code here, and put the code for these in your repo--they will come in handy later.\*\*\***


### Part B
### Construct a simple interaction.

Pick one of the models you have tried, pick a class of objects, and experiment with prototyping an interaction.
This can be as simple as the boat detector earlier.
Try out different interaction outputs and inputs.

**\*\*\*Describe and detail the interaction, as well as your experimentation here.\*\*\***

### interactive Morpheus (from the Matrix) device that dispenses red or blue pills (Candy) based on the users choice.
#### We will specifically be re-creating the scene below and using exact audio from the scene in our device. 

**Major interaction involving the camera and the image recognition models we tried is to detect whether the user is holding a blue pill or a red pill, using the teachable machine. **



https://user-images.githubusercontent.com/73661058/139364599-9e9ed69a-d9c1-4b22-b7e4-0f0195026e1e.mov


- Our device will be made up of a 3D printed Morpheus and cardboard box behind him to store the Pi, camera, motors, and pill dispensors. 
- The way the interaction will work is when the device is turned on Morpheus will start speaking "This is your last chance, after this there is no turning back. You take the blue pill the story ends and you wake up in your bed and belive whatever you want to belive. You take the red pill you stay in wonderland and I show you how deep the rabit hole goes". 
- This will promt the user to choose either a red or blue pill from Morpheus's hands. 
- As the user picks up the pill from Morpheus's hands a camera in the back the box behind Morpheus will detect whether the pill selected is blue or red using a model we trained using trainable machines. 
- Based on the users selection a candy pill will be despensed through a slide at the bottom of the device. 

Device design: 

Front- 

<img width="548" alt="Screen Shot 2021-10-28 at 11 11 44 PM" src="https://user-images.githubusercontent.com/73661058/139367522-cb5e20a9-a646-44f4-a2f1-1fe3dc160553.png">

Back/inside-

<img width="503" alt="Screen Shot 2021-10-28 at 10 54 17 PM" src="https://user-images.githubusercontent.com/73661058/139366050-552c59a1-0333-4ab1-a440-c647f09ece42.png">

Other experimentation and ideations: 
Major things we considered at this stage were where the camera should be placed for the user to be easily recognize where they should be showing the pill, 
where and how the pill should be dispensed, and how things should be layed out behind the board. We were ambitious and excited, so there were a lot to be placed behind the board. We brainstormed a lot about how the image recognition would trigger the dispensing and what physical shape will be most appropriate and feasible for our prototype. 

<img width="463" alt="Screen Shot 2021-10-28 at 11 15 58 PM" src="https://user-images.githubusercontent.com/73661058/139369663-5a6a0543-1146-4472-a3a8-3a94be87e219.png">

<img width="358" alt="Screen Shot 2021-10-28 at 11 15 51 PM" src="https://user-images.githubusercontent.com/73661058/139369888-7d28ded7-385b-4cfe-833e-529e33938e1e.png">

<img width="580" alt="Screen Shot 2021-10-28 at 11 15 38 PM" src="https://user-images.githubusercontent.com/73661058/139369962-c65a8d46-16ed-4412-85cc-0f68cc254c6b.png">

<img width="637" alt="Screen Shot 2021-10-28 at 11 14 42 PM" src="https://user-images.githubusercontent.com/73661058/139370000-4af3b001-422a-4539-ad11-1621b2718cc8.png">

<img width="871" alt="Screen Shot 2021-10-28 at 11 15 22 PM" src="https://user-images.githubusercontent.com/73661058/139369981-0ad65d32-f152-47de-966a-f07a1d36f2d2.png">


### Part C
### Test the interaction prototype

Now flight test your interactive prototype and **note down your observations**:
For example:
1. When does it what it is supposed to do?
    When the user picks up one of the pills, it should be able to detect i) the fact that user has picked up something ii) and the color of the pill
2. When does it fail?
    It fails when the user is holding the pill too far from the camera or holding both of them or not showing it to the camera at at all or pill is not visible to from the camera's angle. Sometimes the user's finger and nails will hide the pill shape and color too much so lead to failure. 
    
3. When it fails, why does it fail?
    Because the model is trained in the case where the user is properly holding the pill, visible to the camera, with the right distance. In the training images, we held the pill pretty close to the camera, not hiding the pill with fingers. 
    Also, some failures were due to the low resolution on Pi camera we're using. We assume that RGB layers are not so strong and it did not recognize red so well sometimes. The model that performed very well with the laptop webcam did not show the same accuracy with the Pi camera. 
   
4. Based on the behavior you have seen, what other scenarios could cause problems?
    The user might not know where the camera is. (I had a laptop and the pi camera on, and it was bit confusing where to look at since the display was on the laptop)
    

<img width="541" alt="Screen Shot 2021-11-02 at 2 16 23 AM" src="https://user-images.githubusercontent.com/42717070/139796302-51d0620d-b8d1-4368-8681-02c42bc25a16.png">
<img width="553" alt="Screen Shot 2021-11-02 at 2 17 01 AM" src="https://user-images.githubusercontent.com/42717070/139796305-b44f4f08-b045-49b3-87a4-e2ea8f40d592.png">


**\*\*\*Think about someone using the system. Describe how you think this will work.\*\*\***
1. Are they aware of the uncertainties in the system?
An educated user who had prior experiences with some image recognition tools might be aware of the uncertainties caused by lighting, distance, and background situation. But we cannot generalize this. An arbitrary user might not be aware of what affects the performance of image/video recognition. Also, when the device does not response for a long time, the user might notice the uncertainties and try to do something. 

2. How bad would they be impacted by a miss classification?
In our prototype miss classification would not be bad, the consquence would just be the user getting a red candy instead of a blue candy or vice versa. However if this was the real matrix and Morphues relied on our classifier the conquences of miss classification would be very severe and life changing.  

3. How could change your interactive system to address this?
We would need to use a more robust classification model to ensure that the model would always easily detect red or blue pills correctly. With our current model we could address this by adding a simple sign that promoted thr user to hold the pill closer to the camera to help mitigate error. 

4. Are there optimizations you can try to do on your sense-making algorithm.
We can add more images from diverse distance and background settings to the training in the first place for more robust performance of recognition algorithm. We can also add other features to recognize like which way the user reaches out their hand, because the red pill is always going to be placed on the left side(when faced).  

### Part D
### Characterize your own Observant system

Now that you have experimented with one or more of these sense-making systems **characterize their behavior**.
During the lecture, we mentioned questions to help characterize a material:
* What can you use X for?
Our device can be used for a fun and interactive way to eat red and blue candy. 
* What is a good environment for X?
A good environment would be in a Matrix enthusiasts' home, perhaps on their desk or coffee table. Ideally when the interaction takes place the backround will be clear so Morpheus camera can clearly see the red or blue pill.  
* What is a bad environment for X?
A Bad environment would be somewhere crowded where the device can not clearly pick up on the detection of the red or blue pill which is essental for the interaction to work correctly. Another bad environmemt would be in ther presents on a non Matrix enthusiasts or Matrix hater. 
* When will X break? / When it breaks how will X break?
The device will break any of its parts stoped working, the camera, the Pi, or the motors. The device would also break if it was phsyically destroyed, Morpheus was smashed or disasembled from his box set up. Anther way the device could break is if the red and blue pills where taken from Morpheus hands, the user would not know what to do or how to interact with the device. Lastly the device would break if the candy it dispenses runs out. 
* What are other properties/behaviors of X?
The device reenacts a classic sense from the Matrix through audio and user interaction. The device has computer vision and detect red and blue pills. The device can make dispensing decsions based on the sight of red or blue pills. The device dispenses red and blue candy. The devive allows for appreciation of the Matrix. 
* How does X feel?
Physically, the devices gives a mysterious Sci-fi vibe, gives the feel of excitement and curiousity from encountering the moment of truth from the movie Matrix!
Emotioanlly, it also feels like delious candy in the users mouth. Also the Matrix theme feels nostalgic. From the material, it feels like a plastic 3D model and cardboard.

**\*\*\*Include a short video demonstrating the answers to these questions.\*\*\***

### Part 2.

Following exploration and reflection from Part 1, finish building your interactive system, and demonstrate it in use with a video.

Work in progress: 
![65812233421__840B57E3-99C9-4218-A28B-C75872413866](https://user-images.githubusercontent.com/73661058/140865540-f993295c-e5cd-432b-ab2b-8f6352a18c30.jpg)
![IMG_7018](https://user-images.githubusercontent.com/73661058/140865548-ef26529e-62b3-4c8f-8b1b-8a7b57b5b9b3.jpg)
![IMG_7015](https://user-images.githubusercontent.com/73661058/140865560-ed654345-f9a3-4e6e-b65d-f64c55265a5b.jpg)
![IMG_7015](https://user-images.githubusercontent.com/73661058/140865563-59d3076c-752b-4c9f-a4bf-453f2edb8608.jpg)
![IMG_6443](https://user-images.githubusercontent.com/73661058/140865568-d628782d-184f-4d96-b1f2-6cde0bd65138.jpg)
![IMG_6462](https://user-images.githubusercontent.com/42717070/140868721-10375c5a-02c4-4b18-b79d-1d501223c773.jpg)

Final Design: 

Front - 
![IMG_7021](https://user-images.githubusercontent.com/73661058/140865621-47396c51-e2cb-4664-84d9-7a948315e0f6.jpg)

Back- 
![IMG_7028](https://user-images.githubusercontent.com/73661058/140865636-b5e1dcbc-5745-459b-866d-98d70d155d37.jpg)

Video-

https://user-images.githubusercontent.com/73661058/140865315-8168582a-f1fa-4041-8eff-4fa0b44ae20b.mov



