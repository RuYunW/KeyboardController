import wx
from pykeyboard import *
import logging
import time
import speech_recognition as sr
# import threading
from threading import Thread
from wx.lib.pubsub import pub as Publisher

logging.basicConfig(level=logging.DEBUG)


class MainWindow(wx.Frame):
    """We simply derive a new class of Frame."""

    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(200, 200))
        self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        self.SetWindowStyle(wx.STAY_ON_TOP)
        self.Show(True)
        # TestThread2()
        # Publisher.subscribe(self.updateDisplay, "update")


        # self.keyboard_controller()

    def updateDisplay(self, msg):
        t = msg.data
        print(t)
        self.control.AppendText(6666)


class TestThread2(Thread):
    def __init__(self):  # 线程实例化时立即启动
        Thread.__init__(self)
        self.start()

    def run(self):
        k = PyKeyboard()
        while True:
            print(666)
            time.sleep(2)





    # def keyboard_controller(self):
    #     k = PyKeyboard()
    #     while True:
    #         r = sr.Recognizer()
    #         mic = sr.Microphone()  # 麦克风
    #         logging.info('录音中...')
    #         self.control.AppendText('录音中...\n')
    #         with mic as source:
    #             r.adjust_for_ambient_noise(source)
    #             audio = r.listen(source)
    #         logging.info('录音结束，识别中...')
    #         self.control.AppendText('录音结束，识别中...\n')
    #         test = r.recognize_google(audio, language='zh-CN', show_all=True)
    #         print(test)
    #         # self.control.AppendText(test)
    #         if len(test) > 0:  # 如果检测到有语音
    #             control = test['alternative'][0]['transcript']
    #             print(control)
    #             self.control.AppendText(control + '\n')
    #
    #             if '向左转' in control:
    #                 k.tap_key('a')
    #             elif '向右转' in control:
    #                 k.tap_key('d')
    #             elif '向后转' in control:
    #                 k.tap_key('s')
    #             elif '前进' in control:
    #                 for i in range(1000):
    #                     k.press_key('w')  # 按住 W 键
    #                 k.release_key('w')
    #             elif '一直跑' in control:
    #                 k.press_key('w')
    #             else:
    #                 pass
    #         else:
    #             continue
    #         logging.info('end')  # 退出登录


class TestThread(Thread):
    def __init__(self):  # 线程实例化时立即启动
        Thread.__init__(self)
        self.start()

    def run(self):
        k = PyKeyboard()
        while True:
            r = sr.Recognizer()
            mic = sr.Microphone()  # 麦克风
            logging.info('录音中...')
            wx.CallAfter(Publisher.sendMessage, 'please speak')
            # self.control.AppendText('录音中...\n')
            with mic as source:
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source)
            logging.info('录音结束，识别中...')
            # self.control.AppendText('录音结束，识别中...\n')
            test = r.recognize_google(audio, language='zh-CN', show_all=True)
            print(test)
            # self.control.AppendText(test)
            if len(test) > 0:  # 如果检测到有语音
                control = test['alternative'][0]['transcript']
                print(control)
                # self.control.AppendText(control + '\n')

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

        # for i in range(101):
        #     time.sleep(0.03)
        #     wx.CallAfter(Publisher.sendMessage, "update", i)
        time.sleep(0.5)
        wx.CallAfter(Publisher.sendMessage, "update", u"线程结束")
