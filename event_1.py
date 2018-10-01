import tkinter
class Tkwin:
    def __init__(self, root):
        self.root = root
        self.frame = tkinter.Frame(root, bd=2)
        self.edit = tkinter.Text(self.frame, width=96, height=32)
        self.edit.pack(side = tkinter.LEFT)
        self.frame.place(y = 50)
        self.edit.bind('<Button-1>', self.action)
    def action(self, event):
        self.edit.insert(tkinter.END, u"窗口坐标x:%d 窗口坐标y:%d\n" % (event.x, event.y))
        self.edit.insert(tkinter.END, u"屏幕坐标x:%d 屏幕坐标y:%d\n" % (event.x_root, event.y_root))

root = tkinter.Tk()
window = Tkwin(root)
root.minsize(600,480)
root.maxsize(600,480)
root.mainloop()