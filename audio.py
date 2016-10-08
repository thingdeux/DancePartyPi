import pyglet
import os

class DancePartyAudioLoadError(Exception):
    pass

class AudioPlayer:
    def __init__(self):
        pyglet.options['audio'] = ('openal', 'pulse')
        self.has_queued_track = False
        self.audio_player = pyglet.media.Player()

    def load_audio(self):
        # Attempt to load the danceparty.mp3 local file - raises MediaException
        try:
            running_directory = os.path.dirname(os.path.realpath(__file__))
            media_path = os.path.join(running_directory, 'media/danceparty.mp3')
            self.dance_party_audio = pyglet.media.load(media_path, streaming=False)
            print("Dance Party Media Loaded")
        except pyglet.media.MediaException as error:
            raise DancePartyAudioLoadError("UNABLE TO LOAD DANCEPARTY.MP3 - {}".format(error))

    def play(self):
        if not self.audio_player.playing and not self.has_queued_track:
            print("Playing Dance Party Track")
            self.audio_player.queue(self.dance_party_audio)
            self.audio_player.play()
            print("Done Playing Audio")
        elif self.has_queued_track and not self.audio_player.playing:
            self.stop()
            self.audio_player.play()

    def stop(self):
        print("Stopping Dance Party Track")
        self.audio_player.pause()
        self.audio_player.seek(0)