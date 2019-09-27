import sounddevice as sd
import soundfile as sf


class RecordAudio:
    def __init__(self):
        self.duration = 5
        self.fs = 44100

    def record(self):
        myrecording = sd.rec(int(self.duration * self.fs), samplerate=self.fs, channels=2)
        sd.wait()
        sf.write('speech.ogg', myrecording, self.fs)

