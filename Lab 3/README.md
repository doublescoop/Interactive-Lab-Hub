# Chatterboxes
[![Watch the video](https://user-images.githubusercontent.com/1128669/135009222-111fe522-e6ba-46ad-b6dc-d1633d21129c.png)](https://www.youtube.com/embed/Q8FWzLMobx0?start=19)

In this lab, we want you to design interaction with a speech-enabled device--something that listens and talks to you. This device can do anything *but* control lights (since we already did that in Lab 1).  First, we want you first to storyboard what you imagine the conversational interaction to be like. Then, you will use wizarding techniques to elicit examples of what people might say, ask, or respond.  We then want you to use the examples collected from at least two other people to inform the redesign of the device.

We will focus on **audio** as the main modality for interaction to start; these general techniques can be extended to **video**, **haptics** or other interactive mechanisms in the second part of the Lab.

## Prep for Part 1: Get the Latest Content and Pick up Additional Parts 

### Pick up Additional Parts

As mentioned during the class, we ordered additional mini microphone for Lab 3. Also, a new part that has finally arrived is encoder! Please remember to pick them up from the TA.

### Get the Latest Content

As always, pull updates from the class Interactive-Lab-Hub to both your Pi and your own GitHub repo. As we discussed in the class, there are 2 ways you can do so:

**\[recommended\]**Option 1: On the Pi, `cd` to your `Interactive-Lab-Hub`, pull the updates from upstream (class lab-hub) and push the updates back to your own GitHub repo. You will need the *personal access token* for this.

```
pi@ixe00:~$ cd Interactive-Lab-Hub
pi@ixe00:~/Interactive-Lab-Hub $ git pull upstream Fall2021
pi@ixe00:~/Interactive-Lab-Hub $ git add .
pi@ixe00:~/Interactive-Lab-Hub $ git commit -m "get lab3 updates"
pi@ixe00:~/Interactive-Lab-Hub $ git push
```

Option 2: On your your own GitHub repo, [create pull request](https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/blob/2021Fall/readings/Submitting%20Labs.md) to get updates from the class Interactive-Lab-Hub. After you have latest updates online, go on your Pi, `cd` to your `Interactive-Lab-Hub` and use `git pull` to get updates from your own GitHub repo.

## Part 1.
### Text to Speech 

In this part of lab, we are going to start peeking into the world of audio on your Pi! 

We will be using a USB microphone, and the speaker on your webcamera. (Originally we intended to use the microphone on the web camera, but it does not seem to work on Linux.) In the home directory of your Pi, there is a folder called `text2speech` containing several shell scripts. `cd` to the folder and list out all the files by `ls`:

```
pi@ixe00:~/text2speech $ ls
Download        festival_demo.sh  GoogleTTS_demo.sh  pico2text_demo.sh
espeak_demo.sh  flite_demo.sh     lookdave.wav
```

You can run these shell files by typing `./filename`, for example, typing `./espeak_demo.sh` and see what happens. Take some time to look at each script and see how it works. You can see a script by typing `cat filename`. For instance:

```
pi@ixe00:~/text2speech $ cat festival_demo.sh 
#from: https://elinux.org/RPi_Text_to_Speech_(Speech_Synthesis)#Festival_Text_to_Speech

echo "Just what do you think you're doing, Dave?" | festival --tts
```

Now, you might wonder what exactly is a `.sh` file? Typically, a `.sh` file is a shell script which you can execute in a terminal. The example files we offer here are for you to figure out the ways to play with audio on your Pi!

You can also play audio files directly with `aplay filename`. Try typing `aplay lookdave.wav`.

\*\***Write your own shell file to use your favorite of these TTS engines to have your Pi greet you by name.**\*\*
(This shell file should be saved to your own repo for this lab.)
Soul: You can find the shell file 'greetme.sh' 

Bonus: If this topic is very exciting to you, you can try out this new TTS system we recently learned about: https://github.com/rhasspy/larynx

### Speech to Text

Now examine the `speech2text` folder. We are using a speech recognition engine, [Vosk](https://alphacephei.com/vosk/), which is made by researchers at Carnegie Mellon University. Vosk is amazing because it is an offline speech recognition engine; that is, all the processing for the speech recognition is happening onboard the Raspberry Pi. 

In particular, look at `test_words.py` and make sure you understand how the vocab is defined. Then try `./vosk_demo_mic.sh`

One thing you might need to pay attention to is the audio input setting of Pi. Since you are plugging the USB cable of your webcam to your Pi at the same time to act as speaker, the default input might be set to the webcam microphone, which will not be working for recording.

\*\***Write your own shell file that verbally asks for a numerical based input (such as a phone number, zipcode, number of pets, etc) and records the answer the respondent provides.**\*\*

Soul: You can find the shell file NumPatty.sh
It asks you how many patties do you want in your burger. 
You can answer in any number below ten (let's be realistic, you can't take more than ten, or even five)

Bonus Activity:

If you are really excited about Speech to Text, you can try out [Mozilla DeepSpeech](https://github.com/mozilla/DeepSpeech) and [voice2json](http://voice2json.org/install.html)
There is an included [dspeech](./dspeech) demo  on the Pi. If you're interested in trying it out, we suggest you create a seperarate virutal environment for it . Create a new Python virtual environment by typing the following commands.

```
pi@ixe00:~ $ virtualenv dspeechexercise
pi@ixe00:~ $ source dspeechexercise/bin/activate
(dspeechexercise) pi@ixe00:~ $ 
```

### Serving Pages

In Lab 1, we served a webpage with flask. In this lab, you may find it useful to serve a webpage for the controller on a remote device. Here is a simple example of a webserver.

```
pi@ixe00:~/Interactive-Lab-Hub/Lab 3 $ python server.py
 * Serving Flask app "server" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 162-573-883
```
From a remote browser on the same network, check to make sure your webserver is working by going to `http://<YourPiIPAddress>:5000`. You should be able to see "Hello World" on the webpage.

### Storyboard

Storyboard and/or use a Verplank diagram to design a speech-enabled device. (Stuck? Make a device that talks for dogs. If that is too stupid, find an application that is better than that.) 

\*\***Post your storyboard and diagram here.**\*\*

I designed a device that can play a 'stroopgame' with the user. Strooptest is a neuropsychological test extensively used to assess the ability to inhibit cognitive interference that occurs when the processing of a specific stimulus feature impedes the simultaneous processing of a second stimulus attribute. In other words, it tests if you can tell the color of the _ink_ correctly when the word reads in different color. So you should say 'pink' when ou see the word 'Black' written in pink ink. 

![IMG_2990](https://user-images.githubusercontent.com/42717070/135952704-f830590e-870d-47b2-b0f9-9ada32764370.jpg)


Write out what you imagine the dialogue to be. Use cards, post-its, or whatever method helps you develop alternatives or group responses.

Imagined dialogues are illustrated in the storyboard above. 
Some alternative dialogues are depicted here:
![IMG_2994](https://user-images.githubusercontent.com/42717070/135952713-1f4d767b-0734-4486-9dc4-36a9260848bd.jpg)

\*\***Please describe and document your process.**\*\*
![IMG_2995](https://user-images.githubusercontent.com/42717070/135952991-2d9d08cc-1977-4694-b9af-7ee12488274f.jpg)
I contemplated on the original storyboard(dialogue script) to find and mark some alternative replies from the users. 
I was able to imagine few alternative situations and narrow them down to few categories. 
   1) user failed to understand the game and asks 'What?' / 'What did you say?' , asking for clarification
   2) user gives half-correct answers in attempt to correct the first reply 
   3) user gives repeated replies since he/she does not know if it's been recorded. I usually call 'Hey Siri' like two three times if it doesn't reply right away and later found out it was on mute but already heard me on the first attempt. Same might happen. 

### Acting out the dialogue

Find a partner, and *without sharing the script with your partner* try out the dialogue you've designed, where you (as the device designer) act as the device you are designing.  Please record this interaction (for example, using Zoom's record feature).


https://user-images.githubusercontent.com/42717070/135952663-41951f1e-d67c-4b18-aa9f-14166516b219.mov



\*\***Describe if the dialogue seemed different than what you imagined when it was acted out, and how.**\*\*

I found some crucial differences in the interaction from what I imagined. 
  1)User does not know what to do when Pi says 'Pick me up'
    I imagined picking up the Pi device and holding it on her/his hand as the first engagement with the Pi. So I designed the Pi to repeatedly say 'Pick me up' until the user does so. However, during the act-out, the user was confused. User didn't expect to have a physical interaction with the device. Also, the user touched the device but didn't hold it in his hand.

  2)User did not expect the game to start right away.
    The design was to start the game right away after giving a one-sentence explanation. However, in the act-out, the user was not sure if the game has alreay begun even when he saw the screen(in the laptop, for this act-out). Therefore the user wasted first 6 seconds, which blew off the first round. 
  
  3)User does not know when the next round starts / how fast should he be.
    The timing of user's reply and the device moving on to the next round was off. By the time the user replies, it was alerady moving on to the next question. I didn't realize there was no clear indication of how fast the user should be answering the question and when it'd move on to the next round.

  4)User thought that repeated 'Pick me up' and 'Bye' at the end is kind of creepy. 
    One-sided communication turned out to be too creepier than I thought. 

  5)User replied 'Red' for the answer in the beginning, since the Pi box is red
    User was asked to tell the Pi 'color of ink you see'. I intended to mean 'what he sees on the screen of Pi', not Pi itself. Unexpected layer of confusion.


One thing I predicted right was:
  User asked back 'What is Strooptest?' When Pi(me) said 'Let's play Strooptest, tell me a color of the ink you see' 


### Wizarding with the Pi (optional)
In the [demo directory](./demo), you will find an example Wizard of Oz project. In that project, you can see how audio and sensor data is streamed from the Pi to a wizard controller that runs in the browser.  You may use this demo code as a template. By running the `app.py` script, you can see how audio and sensor data (Adafruit MPU-6050 6-DoF Accel and Gyro Sensor) is streamed from the Pi to a wizard controller that runs in the browser `http://<YouPiIPAddress>:5000`. You can control what the system says from the controller as well!

\*\***Describe if the dialogue seemed different than what you imagined, or when acted out, when it was wizarded, and how.**\*\*

# Lab 3 Part 2

For Part 2, you will redesign the interaction with the speech-enabled device using the data collected, as well as feedback from part 1.


## Prep for Part 2

1. What are concrete things that could use improvement in the design of your device? For example: wording, timing, anticipation of misunderstandings...

\*\***Things I can improve in design, learned from the act-out**\*\*
  1) Type of Interaction: I designed a game that player's response time is critical. Player with a faster response should be getting a higher score in the 'stroopgame' that I originally wanted to implement with Pi speech interaction. Considering the lagging time of Pi's speech2text function, I should design a different game where there are more verbal interactions with Pi but the response time is less critical in playing.  
  1) Initiation: Instead of repeating 'Pick me up' to start the first interaction, I could use a different nudge to start the engagement.
  2) Explicit Interactions: Add a interaction(user input and feedback) to actively start the game, instead of automatic start. 
  3) Feedback: Add a sign to let the user know when it's moving on to the next round.
  4) Wording: Not use the unfamiliar terminology 'Stroopgame'. Change the instruction to be more self-explanatory.

\*\***Learned from the feedback**\*\*
 1. Stroop doesn't require so much of speech interactions. I could design a more verbally interactive situation. 



2. What are other modes of interaction _beyond speech_ that you might also use to clarify how to interact?
  1) Written communication: adding a written description next to Pi device clarifying how to initiate conversation or how it might take few seconds for Pi to understand the player
  2) Visual sign: using LED light to signal the player when they gave a correct answer during the game
  3) Visual sign: using an arrow icon to mark the location of the microphone.


3. Make a new storyboard, diagram and/or script based on these reflections.

## Prototype your system

The system should:
* use the Raspberry Pi 
* use one or more sensors
* require participants to speak to it. 

*Document how the system works*

*Include videos or screencaptures of both the system and the controller.*

## Test the system
Try to get at least two people to interact with your system. (Ideally, you would inform them that there is a wizard _after_ the interaction, but we recognize that can be hard.)

Answer the following:

### What worked well about the system and what didn't?
\*\**Directing the player to speak closer to the microphone when the first recording from the user was not clear worked well. Players tried to speak louder and closer to the microphone after the instruction. Verbally explaining what game the Pi wants to play to the user went well too. Players understood they have to guess the drawing on the screen and spoke out loud their answers. However, sometimes Pi didn't recognize correct answers. It might be due to low recording quality.*\*\*

### What worked well about the controller and what didn't?

\*\**In my design, I didn't have to use a controller. Pi and the player initiated and continued verbal interactions. Player's reply or preset timer triggered next scene.*\*\*

### What lessons can you take away from the WoZ interactions for designing a more autonomous version of the system?

\*\**Utilizing an appropriate sensors and libraries that resonate with natural way of interaction is critical. For example, I first tried to initiate the interaction by having the player to phisically 'pick up' the Pi, in attempt to get the player closer to the microphone. However, it confused the player and failed to initiate the interaction since the players are not used to the action of picking up the device to start interacting. In autonomous design, it would be more critical to devise a system that follows the player's natural way of thinking. 
Also, giving an explicit feedback after the player's action(speaking) is crucial. In autonomous design, the user might not know whether something is being processed behind the scene or not. For example, it took Pi about 5 seconds to process and dictate(speech2text) the plyers's reply and judge if it's correct. Players got impaitient during the wait or were wondering if it's working. Therefore, while the autonomous process is happening, there should be a signal to inform the user about it. *\*\*


### How could you use your system to create a dataset of interaction? What other sensing modalities would make sense to capture?

\*\** It could create a dataset that captures how humans follow directions from a robot and how they react to it. Partially due to the limitation of microphone quality and size of the screen, my system required the user to adopt an unnatural way of interaction(having to bend down and speack very close to a device/repeating the same reply etc). I think it would collect interesting reactions from users how well/badly they follow the directions given by the Pi('get really close to me and speak louder) and what's their reactions. It's not a sensing modality but capturing their facial expressions during this interaction would make sense to further analyze how they feel and react. 

Also, my system is trying to stimuly users' emotions towards a robot through the interaction. It could be used to create a dataset of emotional impacts created by the interaction. For example, I used a rather cute disguise for the device and implemented emotional quotes like 'it'd warm my heart up' to create some emotional conncections during the interaction. There are no sensory modalities needed other than the sound but capturing heart rate, facial expressions, or ideally brain waves can help investigating emotional impacts. *\*\*

