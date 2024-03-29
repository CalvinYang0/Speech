from nlp.snowboy_kws import snowboydecoder as snowboydecoder
import signal

interrupted = False


def signal_handler(signal, frame):
    global interrupted
    interrupted = True


def interrupt_callback():
    global interrupted
    return interrupted


def getSentence():
    print("yes")


class SnowboyKWS:
    def run(self,function=snowboydecoder.play_audio_file()):
        # 模型路径
        model = "robot.pmdl"
        # capture SIGINT signal, e.g., Ctrl+C
        signal.signal(signal.SIGINT, signal_handler)

        detector = snowboydecoder.HotwordDetector(model, sensitivity=0.5)
        print('Listening... Press Ctrl+C to exit')

        # main loop
        if function==None:
            detector.start(detected_callback=function,
                           interrupt_check=interrupt_callback,
                           sleep_time=0.03)
        else:
            detector.start(detected_callback=function,
                           interrupt_check=interrupt_callback,
                           sleep_time=0.03)
        detector.terminate()


if __name__ == '__main__':
    snowboy_vad = SnowboyKWS()
    snowboy_vad.run()
