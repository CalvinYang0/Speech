
class ASR:
    """
        Asr类用于语音识别
        使用时需要单开线程
        如果这是个需要加载模型的load_asr_model函数需要被提前启用，以减少加载模型带来的时间损耗
        后台等待音频传入，调用analyse_audio函数进行识别返回文本
    """

    def load_asr_model(self):
        pass

    def analyse_audio(self, audio):
        pass

    def __init__(self):
        self.load_asr_model()


if __name__ == "__main__":
    # 命令行输入音频的名称，输出结果
    pass
