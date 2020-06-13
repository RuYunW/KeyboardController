import speech_recognition as sr
import logging
from pykeyboard import *
import time

# logging.basicConfig(level=logging.DEBUG)
k = PyKeyboard()

def run_all_time():
    k.press_key('w')
    while True:
        r = sr.Recognizer()
        mic = sr.Microphone()
        logging.info('录音中...')
        with mic as source:
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
        logging.info('录音结束，识别中...')
        test = r.recognize_google(audio, language='zh-CN', show_all=True)
        if len(test) > 0:  # 如果检测到有语音
            control = test['alternative'][0]['transcript']
            if '停' in control:
                k.release_key('w')
                k.tab_key('s')
                break
        else:
            continue

