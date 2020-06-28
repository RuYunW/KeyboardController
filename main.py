from wind import *
import wx
import _thread
from kb_ctrler import keyboard_controller


app = wx.App(False)
frame = MainWindow(None, 'Message Table')
try:
    _thread.start_new_thread(keyboard_controller, (frame, ))
except:
    print("Error: 无法启动线程")

app.MainLoop()





