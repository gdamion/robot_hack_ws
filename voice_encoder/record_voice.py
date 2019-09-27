import sounddevice as sd
import soundfile as sf
from scipy.io.wavfile import write


class RecordAudio:
    def __init__(self):
        self.duration = 3
        self.fs = 44100

    def record(self):
        myrecording = sd.rec(int(self.duration * self.fs), samplerate=self.fs, channels=2)
        sd.wait()
        write('output.wav', self.fs, myrecording)
        data, samplerate = sf.read('output.wav')
        sf.write('speech.ogg', data, samplerate)
