import wx
import json
from selenium_util import getLinks
from bs4_util import getYouTubeVideoStats
from firestore_util import addDocument

class App(wx.Frame):

    def __init__(self):
        super().__init__(parent=None, title='EDUKID',size=(400, 450),style=wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION |	 wx.CLOSE_BOX)
        self.Centre()
        panel = wx.Panel(self,wx.ID_ANY,wx.Point(),wx.Size(300,600))
        my_sizer = wx.BoxSizer(wx.VERTICAL)
        lbl = wx.StaticText(panel,-1,style = wx.ALIGN_CENTER)

        txt1 = "\nYouTube\n"

        font = wx.Font(18, wx.ROMAN, wx.BOLD, wx.NORMAL)
        font1 = wx.Font(15, wx.ROMAN, wx.NORMAL,wx.NORMAL)
        lbl.SetFont(font)
        lbl.SetLabel(txt1)
        lbl.SetForegroundColour(wx.Colour(245, 71, 72))

        my_sizer.Add(lbl,0,wx.ALIGN_CENTER)
        self.text_ctrl = wx.TextCtrl(panel,wx.ID_ANY,size=(200,50),style = wx.TE_MULTILINE)
        self.text_ctrl.SetFont(font1)
        my_sizer.Add(self.text_ctrl,0, wx.ALL | wx.EXPAND, 5)

        lbl_logs = wx.StaticText(panel,-1,style = wx.ALIGN_CENTER)
        lbl_logs.SetFont(font1)
        lbl_logs.SetLabel("\nLogs")
        my_sizer.Add(lbl_logs,0)

        self.logs = wx.TextCtrl(panel,wx.ID_ANY,size=(200,180),style = wx.TE_MULTILINE | wx.TE_READONLY)
        self.logs.SetFont(font1)
        my_sizer.Add(self.logs,0, wx.ALL | wx.EXPAND, 5)

        self.my_btn = wx.Button(panel,wx.ID_ANY,size=(100,35), label='SUBMIT')
        my_sizer.Add(self.my_btn, 0, wx.ALL | wx.CENTER, 5)
        panel.SetSizer(my_sizer)

        self.status = wx.StaticText(panel,-1,style = wx.ALIGN_CENTER,pos=(5,400))
        self.status.SetFont(font1)
        self.status.SetLabel("Enter what you want to srape from YouTube.")
        self.status.SetForegroundColour(wx.Colour(255,0,0))

        def processing():
            self.status.SetLabel("Processing ...,This will take few minutes")
            self.my_btn.Disable()


        def completed():
            self.status.SetLabel("Enter what you want to srape from YouTube.")
            self.my_btn.Enable()

        def addLogs(text):
            currentCaretPosition = self.logs.GetInsertionPoint()
            currentLengthOfText = self.logs.GetLastPosition()
            if currentCaretPosition != currentLengthOfText:
                self.holdingBack = True
            else:
                self.holdingBack = False

            if self.holdingBack:
                self.logger.Freeze()
                (currentSelectionStart, currentSelectionEnd) = self.logger.GetSelection()
                self.logs.AppendText(text+"\n")
                self.logs.SetInsertionPoint(currentCaretPosition)
                self.logs.SetSelection(currentSelectionStart, currentSelectionEnd)
                self.logs.Thaw()
            else:
                self.logs.AppendText(text+"\n")

        def onclick(event):
            processing()
            keywords = self.text_ctrl.GetValue().strip()
            if keywords == "":
                wx.MessageBox('No keywords!', 'Info', wx.OK | wx.ICON_INFORMATION)
            else:
                wx.MessageBox('This will take few minutes', 'Info', wx.OK | wx.ICON_INFORMATION)
                links = getLinks(keywords)
                for link in links:
                    if type(link) is str:
                        addLogs('Call for ' + link + '\n')
                        stat = getYouTubeVideoStats(link)
                        if stat['videoID'] and stat['videoTitle'] and stat['videoUrl']:
                            addLogs(json.dumps(stat))
                            addDocument(stat)
                        else:
                            addLogs("Failed to scrape ...")
                        addLogs('\n')
            completed()

        self.Bind(wx.EVT_BUTTON,onclick,self.my_btn)
        self.Show()


if __name__ == '__main__':
    app = wx.App()
    frame = App()
    app.MainLoop()
