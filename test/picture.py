# coding=utf-8

# 点击按钮退出（例子1）

# # 引入Tkinter 包的所有内容
# from Tkinter import *
#
# # 从Frame派生一个Application类
# class Application(Frame):
#     def __init__(self, master=None):
#         Frame.__init__(self, master)
#         self.pack()
#         self.createWidgets()
#
#     def createWidgets(self):
#         self.helloLabel = Label(self, text='hello, world!')
#         self.helloLabel.pack()
#         self.quitButton = Button(self, text='Quit', command=self.quit)
#         self.quitButton.pack()
#
# # 实例化Application
# app = Application()
#
# app.master.title('hello world')

# # 主消息循环
# app.mainloop()

# 点击按钮弹出窗口（例子2）
from Tkinter import *
import tkMessageBox

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.alertButton = Button(self, text='点击', command=self.hello)
        self.alertButton.pack()

    def hello(self):
        name = self.nameInput.get() or 'world'
        tkMessageBox.showinfo('Message', 'hello %s' % name)

app = Application()
app.master.title('hello')
app.mainloop()