import requests
from record_voice import RecordAudio


class VoiceRecognition(RecordAudio):
    def __init__(self):
        RecordAudio.__init__(self)
        self.FOLDER_ID = 'b1g7ddufo2uj17ecq437'
        self.IAM_TOKEN = "CggaATEVAgAAABKABGOvdeSwb-9Ay5swyxrZ2PMH4MvN9osHtkKdaWR6Y7c5-WDkNZcbgLI5U8CLQGxkV6StaaLcDdSmEBF9MvkeQrR-V0Mu9ruC0\
ukzJmuH0MV9jCQVIQFScBh95RjJO32JTYWzmom0m3FheF_ZQuRv_MQPku9qFzlxJZ5epIA_ye403OKT-iaokEGsY-DyNBIy1Zl6SkGpYnCTat2iLyWWyzuZF7h8D4rQ\
XtG2My5V7q2Q7cQpnzDCbMyMvks3KeIZVf_Vl9rrHH6dXSX3oyYJMPhe43Qp4PFPVEcEVCR48twsgq8oHJDQhAxUpycu1G1Yb2QkaK9xQtObiOnw0s4JD78PGZS_QFP\
GyNtxLRdPywUHliw0gkmkTgQsCfwJBmWGK66TmoxQYRgxG9waxh24skXMo85dk2Lja0XiVx10-tWj2XGWShhFg0jfFe29jLzhpkApFjXvRgCyaHiuqtD_XlzxHyfQi6\
pnPkIUF4j6OuDORJy2PaKULaBB41JjWFaWTR_blbqErKLG32GCzjjt23r2d2nCjbln4JeIi1baV-yL1IjOwkZ9bQZPDi-6rA6XYNZ-p3bAlI-a5QYmMeOOimn7X65FU\
14inee1mv88qoCfMIBZtwq77aw4NMa5f5vYu32Hh9JqhygbxOf9AsyJacUQOMwcakomgctmyiq08-VCGmEKIGI5MDYyZmY4ZTMxMzQzZmJhODFkODMxYjA0MGUxYjMw\
EI79t-wFGM7OuuwFIh8KFGFqZWpxMjRrcjhka2xhcGo1Y3NsEgdnb2R6aGFuWgAwAjgBSggaATEVAgAAAFABIPAE"
        self.url = "https://stt.api.cloud.yandex.net/speech/v1/stt:recognize"

    def get_voice(self):
        self.record()
        with open("speech.ogg", "rb") as f:
            data = f.read()
        params = {'topic': 'general', 'folderId': self.FOLDER_ID, 'lang': 'ru-RU'}
        headers = {'Authorization': 'Bearer ' + self.IAM_TOKEN}
        x = requests.post(self.url, params=params, data=data, headers=headers)
        return x.json()['result']


