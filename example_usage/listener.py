from nlp.automatic_speech_recognition.asr import ASR
from nlp.information_extraction.text_processor import TextProcessor
from nlp.sound_recorder.sound_recorder import SoundRecorder
from nlp.text_to_speech.audio_player import AudioPlayer


class Listener:
    """
    这是一个单线程版本，不预先加载资源，不使用命令词唤醒
    """

    def listen_once(self):
        # 播放提示音，提示引导者说话
        audio_player = AudioPlayer()
        audio_player.play_audio("Please give your instructions.")
        # 录音
        sound_recorder = SoundRecorder()
        sound = sound_recorder.record_sound()
        # 语音识别
        asr = ASR()
        text = asr.analyse_audio(sound)
        # 信息抽取
        text_processor = TextProcessor()
        result = text_processor.information_extraction(text)
        # 返回结果
        return result


if __name__ == "__main__":
    listener = Listener()
    print(listener.listen_once())
