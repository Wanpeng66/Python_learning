# 使用内置的Tkinter来编写一个GUI版本的“Hello, world!”
from tkinter import *
from tkinter import messagebox


class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self,master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.quitButton = Button(self, text='hello', command=self.hello)
        self.quitButton.pack()

    def hello(self):
        name = self.nameInput.get() or "world"
        messagebox.showinfo('Message', 'Hello, %s' % name)


if __name__ == "__main__":
    app = Application()
    # 设置窗口标题:
    app.master.title('Hello World')
    # 主消息循环:
    app.mainloop()