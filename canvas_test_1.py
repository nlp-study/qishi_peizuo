from  tkinter import *
from PIL import Image,ImageTk

def show(event):
    img = Image.open("data/dizuo/2.jpg")
    img = ImageTk.PhotoImage(img)
    im = can.create_image(250, 150, image=img)
    l=can.create_line(10,10,50,50,width=5)



root=Tk()
root.title('Canvas')
can=Canvas(root,bg='blue')
# can.create_line(10,10,50,50)
can.grid()
button=Button(height=1,width=20,text='button',bg='red')
button.bind("<Button-1>",show)
button.grid()


root.mainloop()