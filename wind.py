import wx

class MyApp(wx.App):
    def OnInit(self):  #初始化接口，子类覆盖父类的方法
        frame=wx.Frame(parent=None,title="hello wxpython")  #新建框架
        frame.Show()  #显示
        return True