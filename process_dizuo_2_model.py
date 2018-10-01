from tkinter import *
from PIL import Image,ImageTk


def resize(w, h, w_box, h_box, pil_image):
    '''
    resize a pil_image object so it will fit into
    a box of size w_box times h_box, but retain aspect ratio
    对一个pil_image对象进行缩放，让它在一个矩形框内，还能保持比例
    '''
    f1 = 1.0 * w_box / w  # 1.0 forces float division in Python2
    f2 = 1.0 * h_box / h
    factor = min([f1, f2])
    # print(f1, f2, factor) # test
    # use best down-sizing filter
    width = int(w * factor)
    height = int(h * factor)
    return pil_image.resize((width, height), Image.ANTIALIAS),factor

class Window(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title('第一个窗体')
        self.pack(fill=BOTH,expand=1)

        # menu = Menu(self.master)
        # self.master.config(menu = menu)
        self.file_path = "data/dizuo/21.jpg"

        self.init_canvas()

        self.build_buttons()


    def init_canvas(self):
        self.w_canvas = 600
        self.h_canvas = 600
        self.canvas = Canvas(self,bg='red',height = self.h_canvas,width = self.w_canvas)
        self.canvas.grid()


    def build_buttons(self):
        self.button1 = Button(height=1, width=20, text='加载底座', bg='red')
        self.button1.bind("<Button-1>", self.showImage)
        self.button1.pack()

        self.button2 = Button(height=1, width=20, text='设置入口点', bg='red')
        self.button2.bind("<Button-1>", self.set_entrance_points)
        self.button2.pack()

        self.button3 = Button(height=1, width=20, text='保存模型', bg='red')
        self.button3.bind("<Button-1>", self.save_model)
        self.button3.pack()


    def showImage(self,event):


        self.img = Image.open(self.file_path)
        self.img = ImageTk.PhotoImage(self.img)
        im = self.canvas.create_image(0, 0, image=self.img)
        self.canvas.pack()


        #
        # self.pil_image = Image.open(self.file_path)
        #
        # w, h = self.pil_image.size
        # print('dafadfsssssssssssssssssss1')
        # # self.pil_image_resized,factor = resize(w, h, w_box, h_box, self.pil_image)
        # print('dafadfsssssssssssssssssss2')
        #
        # self.img = ImageTk.PhotoImage(self.pil_image)
        # print('dafadfsssssssssssssssssss3')

        # im = self.canvas.create_image(w_box, h_box, image=self.img)
        # print('dafadfsssssssssssssssssss4')
        # self.canvas.pack()

    def set_entrance_points(self,event):
        print('设置底座入口点')

    def save_model(self,event):
        print('保存模型')






    def client_exit(self):
        exit()





root  = Tk()
root.geometry("800x700")
app = Window(root)
root.mainloop()




