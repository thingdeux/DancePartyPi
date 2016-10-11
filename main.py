#!/usr/bin/env python3
from speech_recognition import Recognizer, Microphone
import speech_recognition as sr
from audio import AudioPlayer, DancePartyAudioLoadError
import time
import threading

dance_party_audio = AudioPlayer()

# NOTE: Called on a background thread
def onAudioReceived(recognizer, audio):
    # received audio data, now we'll recognize it using Google Speech Recognition
    try:
        # Keyword argument 'key' can be passed to recognize_google to use API key for cloud speech.
        recognized_audio = recognizer.recognize_google(audio)
        # recognized_audio = recognizer.recognize_sphinx(audio)
        print("Google Speech Recognition thinks you said " + recognized_audio)

        if "dance party" in str(recognized_audio).lower():
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
        recognizer.energy_threshold = 200

        microphone = Microphone()
        with microphone as source:
            recognizer.adjust_for_ambient_noise(source)

        # start listening on the mic
        stop_listening = recognizer.listen_in_background(microphone, onAudioReceived)
        while True:
            # "Block" the main thread ... will run additional logic to handle
            # Hardware here - TODO
            time.sleep(0.1)
        # Kill the background listener stop listening
        stop_listening()
    except DancePartyAudioLoadError as error:
        print(error)




