import wx


class MainWindow(wx.Frame):
    """We simply derive a new class of Frame."""
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(200, 200))
        self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        for i in range(10):
            self.control.AppendText('hi\n')
        self.Show(True)