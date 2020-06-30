import speech_recognition as sr
import logging
from pykeyboard import *
from win32api import keybd_event
from win32con import KEYEVENTF_KEYUP
import time
from threading import Thread
from kb import key_press, key_down, key_up, SPkey_down, SPkey_up

logging.basicConfig(level=logging.DEBUG)


def keyboard_controller(frame):
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
                key_press(0x1E, 0.1)  # A * 0.1

            elif '向左走' in control:
                key_press(0x1E, 1)  # A * 1.0

            elif '向右转' in control:
                key_press(0x20, 0.1)  # D * 0.1

            elif '向右走' in control:
                key_press(0x20, 1)  # D * 1.0

            elif '向后转' in control:
                key_press(0x1F, 0.1)  # S * 0.1

            elif '向前走' in control:
                key_press(0x11, 1)  # W * 1.0

            elif '一直跑' in control:
                key_down(0x11)  # W * 3.0
                time.sleep(0.5)
                key_up(0x11)
                key_down(0x11)  # W
                time.sleep(0.5)
                key_up(0x11)
                key_down(0x11)  # W
                time.sleep(0.5)
                key_up(0x11)
                key_down(0x11)  # W
                time.sleep(0.5)
                key_up(0x11)
                key_down(0x11)  # W
                time.sleep(0.5)
                key_up(0x11)
                key_down(0x11)  # W
                time.sleep(0.5)
                key_up(0x11)

            elif '后退' in control:
                key_press(0x1F, 1)  # S

            elif '向前跳' in control:
                key_down(0x11)  # W
                key_press(0x39, 0.5)  # space
                key_up(0x11)

        else:
            continue
        logging.info('end')  # 退出登录
