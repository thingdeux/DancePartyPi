import pyglet
import os

class DancePartyAudioLoadError(Exception):
    pass

class AudioPlayer:
    def __init__(self):
        pyglet.options['audio'] = ('openal')

    def load_audio(self):
        try:
            running_directory = os.path.dirname(os.path.realpath(__file__))
            media_path = os.path.join(running_directory, 'media/danceparty.mp3')
            self.dance_party_audio = pyglet.media.load(media_path, streaming=False)
            print("Dance Party Media Loaded")
        except pyglet.media.MediaException as error:
            raise DancePartyAudioLoadError("UNABLE TO LOAD DANCEPARTY.MP3 - {}".format(error))

    def play(self):
        print("Playing Dance Party")
        self.dance_party_audio.play()
