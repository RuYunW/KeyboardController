from wind import *
import wx
import _thread
from kb_ctrler import keyboard_controller
from app_open import app_open


app_dir = r'G:\Unity3D项目\My1stGame.exe'
app = wx.App(False)
frame = MainWindow(None, 'Message Table')
try:
    _thread.start_new_thread(keyboard_controller, (frame, ))
except:
    print("Error: 无法启动线程")

app_open(app_dir)
app.MainLoop()





