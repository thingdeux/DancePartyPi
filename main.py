#!/usr/bin/env python3
from speech_recognition import Recognizer, Microphone
import speech_recognition as sr
from audio import AudioPlayer, DancePartyAudioLoadError
import time
import threading

dance_party_audio = AudioPlayer()

# this is called from the background thread
def onAudioReceived(recognizer, audio):
    # received audio data, now we'll recognize it using Google Speech Recognition
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        recognized_audio = recognizer.recognize_google(audio)
        print("Google Speech Recognition thinks you said " + recognized_audio)
        if "dance party" in recognized_audio:
            dance_party_audio.play()

    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

# Listen for voice audio in a loop and wait for the word 'Dance party'
if __name__ == '__main__':
    try:
        dance_party_audio.load_audio()
        recognizer = Recognizer()
        microphone = Microphone()
        with microphone as source:
            recognizer.adjust_for_ambient_noise(source)  # we only need to calibrate once, before we start listening

        # start listening in the background
        stop_listening = recognizer.listen_in_background(microphone, onAudioReceived)
        while True:
            time.sleep(0.1)
        stop_listening()  # calling this function requests that the background listener stop listening
    except DancePartyAudioLoadError as error:
        print(error)




