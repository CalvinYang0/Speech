from nlp.automatic_speech_recognition.asr import WhisperAsr
from nlp.information_extraction import text_processor
# from nlp.keyword_spotting import picovoice_kws
from nlp.sound_recorder.webrtc_vad import WebrtcVad
from nlp.text_to_speech.audio_player import EspeakAudioPlayer


class Listener:
    """
    这是一个单线程版本，不预先加载资源，不使用命令词唤醒
    """

    def __init__(self):
        self.name_list = ["Mike", "John", "Calvin", "Amy", "Elizabeth"]
        self.drink_list = ['juice', 'water', 'milk', 'tea', 'cola']
        self.asr = WhisperAsr()
        self.asr.load_asr_model()
        self.audio_player = EspeakAudioPlayer()

    def ask_name(self):
        # 播放提示音，提示引导者说话
        self.audio_player.play_audio("What is your name ？")
        vad = WebrtcVad()
        vad.run()
        print("识别结果")
        text = self.asr.audio2text("vad.wav")
        print(text)
        for letter in [',', '.', '?', '!']:
            text.replace(letter, " ")
        text_list = text.split()
        name = text_processor.TextProcessor.find_keyword_in_list(text_list, self.name_list)
        if name == None:
            self.audio_player.play_audio("I can not understand.")
        else:
            self.audio_player.play_audio("Hello" + name)
        return name

    def ask_favourite_drink(self):
        # 播放提示音，提示引导者说话
        self.audio_player.play_audio("What is your favourite drink ？")
        vad = WebrtcVad()
        vad.run()
        print("识别结果")
        text = self.asr.audio2text("vad.wav")
        print(text)
        for letter in [',', '.', '?', '!']:
            text.replace(letter, " ")
        text_list = text.split()
        drink = text_processor.TextProcessor.find_keyword_in_list(text_list, self.drink_list)
        if drink == None:
            self.audio_player.play_audio("I can not understand.")
        else:
            self.audio_player.play_audio("Your favourite drink is " + drink)
        return drink


if __name__ == "__main__":
    listener = Listener()
    print("\n", listener.ask_name())
