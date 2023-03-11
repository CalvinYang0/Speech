from nlp.automatic_speech_recognition.asr import WhisperAsr
from nlp.information_extraction import text_processor
# from nlp.keyword_spotting import picovoice_kws
from nlp.sound_recorder.webrtc_vad import WebrtcVad
from nlp.text_to_speech.audio_player import EspeakAudioPlayer
from nlp.keyword_spotting.snowboy_kws import SnowboyKWS


class Listener:
    """
    这是一个单线程版本，不预先加载资源，不使用命令词唤醒
    """

    def __init__(self):
        self.object_list = ['soap', 'chips', 'sprite']
        self.follow_list = ['follow', 'chase', 'Follow', 'Chase']
        self.asr = WhisperAsr()
        self.asr.load_asr_model()
        self.audio_player = EspeakAudioPlayer()

    def what_is_here(self):
        # 播放提示音，提示引导者说话
        kws = SnowboyKWS()
        kws.run()

        self.audio_player.play_audio("What is here?")
        vad = WebrtcVad()
        vad.run()
        print("识别结果")
        text = self.asr.audio2text("vad.wav")
        print(text)
        for letter in [',', '.', '?', '!']:
            text = text.replace(letter, " ")
        text_list = text.split()
        object = text_processor.TextProcessor.find_keyword_in_list(text_list, self.object_list)

        if object == None:
            self.audio_player.play_audio("I can not understand.")
        else:
            self.audio_player.play_audio(object + " is here.")
            print(object + "is here.")
        return object

    def already_find(self, obj):
        self.audio_player.play_audio("I find " + obj)

    def wait_guide(self):
        kws = SnowboyKWS()
        kws.run()
        self.audio_player.play_audio("I am here.")
        vad = WebrtcVad()
        vad.run()
        print("识别结果")
        text = self.asr.audio2text("vad.wav")
        print(text)
        for letter in [',', '.', '?', '!']:
            text = text.replace(letter, " ")
        text_list = text.split()
        instruction = text_processor.TextProcessor.find_keyword_in_list(text_list, self.follow_list)

        if instruction == None:
            self.audio_player.play_audio("I can not understand.")
            return instruction
        else:
            self.audio_player.play_audio("I will follow you.")
            print("Follow")
            return instruction.lower()
def shopping_test():
    listener=Listener();
    while (listener.wait_guide()==None):
        pass
    for i in range(3):
        while (listener.what_is_here()==None):
            pass


if __name__ == "__main__":
    shopping_test()
