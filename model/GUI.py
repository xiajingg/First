#图形界面
from tkinter import *


class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidges()

    def createWidges(self):
        self.helloLabel = Label(self, text='夏晶是个大傻子！')
        self.helloLabel.pack()
        self.quitButtion = Button(self, text='你说的好对哟,他傻不啦叽的', command=self.quit)
        self.quitButtion.pack()


app = Application()
app.master.title('夏晶是个什么样的人?')
app.mainloop()
