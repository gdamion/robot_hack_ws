import pyaudio


class RecordAudio:
    def __init__(self):
        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = 2
        self.RATE = 44100
        self.CHUNK = 1024
        self.RECORD_SECONDS = 5
        self.audio = pyaudio.PyAudio()

    def record(self):
        # start Recording
        stream = self.audio.open(format=self.FORMAT, channels=self.CHANNELS,
                            rate=self.RATE, input=True,
                            frames_per_buffer=self.CHUNK)
        print "recording..."
        frames = []

        for i in range(0, int(self.RATE / self.CHUNK * self.RECORD_SECONDS)):
            data = stream.read(self.CHUNK)
            frames.append(data)
        print "finished recording"

        # stop Recording
        stream.stop_stream()
        stream.close()
        self.audio.terminate()
        return b''.join(frames)
