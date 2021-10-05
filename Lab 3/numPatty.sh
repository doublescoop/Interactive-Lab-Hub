#Ask a question

#from: https://elinux.org/RPi_Text_to_Speech_(Speech_Synthesis)#Festival_Tex$

echo "how many patties do you want in your burger?" | festival --tts



#Record the Answer
#arecord -f cd -r 16000 -d 5 -t wav recorded.wav && sox recorded.wav recorde$


arecord -D hw:2,0 -f cd -c1 -r 48000 -d 5 -t wav recorded_mono.wav
python3 test_words.py recorded_mono.wav
