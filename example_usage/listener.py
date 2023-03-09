from nlp.text_to_speech.audio_player import EspeakAudioPlayer
from nlp.automatic_speech_recognition.asr import WhisperAsr
# from nlp.keyword_spotting import picovoice_kws
from nlp.sound_recorder.webrtc_vad import WebrtcVad
from nlp.keyword_spotting.snowboy_vad import SnowboyKWS


class Listener:
    """
    这是一个单线程版本，不预先加载资源，不使用命令词唤醒
    """

    def listen_once(self):
        # 播放提示音，提示引导者说话
        asr = WhisperAsr()
        asr.load_asr_model()
        audio_player = EspeakAudioPlayer()

        audio_player.play_audio("Please give your instructions.")
        kws = SnowboyKWS()
        kws.run()
        audio_player.play_audio("I am here.")
        vad = WebrtcVad()

        vad.run()
        print("识别结束")
        text = asr.audio2text("vad.wav")
        return text


if __name__ == "__main__":
    listener = Listener()
    print("\n", listener.listen_once())
