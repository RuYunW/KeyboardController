import speech_recognition as sr
import logging
from pykeyboard import *
import time
from threading import Thread

logging.basicConfig(level=logging.DEBUG)
k = PyKeyboard()


def keyboard_controller(frame):
    k = PyKeyboard()
    while True:
        r = sr.Recognizer()
        mic = sr.Microphone()  # 麦克风
        logging.info('录音中...')
        frame.control.AppendText('录音中...\n')
        with mic as source:
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
        logging.info('录音结束，识别中...')
        frame.control.AppendText('录音结束，识别中...\n')
        test = r.recognize_google(audio, language='zh-CN', show_all=True)
        print(test)
        # self.control.AppendText(test)
        if len(test) > 0:  # 如果检测到有语音
            control = test['alternative'][0]['transcript']
            print(control)
            frame.control.AppendText(control + '\n')

            if '向左转' in control:
                k.tap_key('a')
            elif '向右转' in control:
                k.tap_key('d')
            elif '向后转' in control:
                k.tap_key('s')
            elif '前进' in control:
                for i in range(1000):
                    k.press_key('w')  # 按住 W 键
                k.release_key('w')
            elif '一直跑' in control:
                k.press_key('w')
            else:
                pass
        else:
            continue
        logging.info('end')  # 退出登录
