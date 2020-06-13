import speech_recognition as sr
import logging
from pykeyboard import *
import time
from funcs import run_all_time

logging.basicConfig(level=logging.DEBUG)
k = PyKeyboard()

while True:
    r = sr.Recognizer()
    # 麦克风
    mic = sr.Microphone()

    logging.info('录音中...')
    with mic as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    logging.info('录音结束，识别中...')
    test = r.recognize_google(audio, language='zh-CN', show_all=True)
    print(test)
    if len(test)>0:  # 如果检测到有语音
        control = test['alternative'][0]['transcript']
        print(control)
        if '向左转' in control:
            k.tap_key('a')
        elif '向右转' in control:
            k.tap_key('d')
        elif '向后转' in control:
            k.tap_key('s')
        elif '前进' in control:
            k.press_key('w')  # 按住 W 键两秒
            time.sleep(2)
            k.release_key('w')
        elif '一直跑' in control:

        else:
            pass
    else:
        continue

    logging.info('end')  # 退出登录

