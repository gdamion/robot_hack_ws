# coding=utf-8
from voice_recognition import VoiceRecognition
import re

class EncodeCommands(VoiceRecognition):
    def __init__(self):
        VoiceRecognition.__init__(self)

    def encode(self):
        pattern = ur'принеси с кухни (\w*?) губку'
        prog = re.compile(pattern, re.UNICODE)
        while True:
            data = self.get_voice()
            print(data)
            res = prog.match(data)
            if bool(res):
                return res.group(1)
