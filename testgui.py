from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog

root = Tk()
root.title("Welcome to Our Colorization Tool")
root.geometry("500x500")
root.configure(background='light blue')


def browsefunc():
    filename = filedialog.askopenfilename()
    pathlabel.config(text=filename)
    canvas = Canvas(root)
    canvas.pack()
    img = ImageTk.PhotoImage(file = filename)
    canvas.create_image(20, 20, anchor=NW, image = img)
    # look for a .draw function

browsebutton = Button(root, text="Browse", command=browsefunc)
browsebutton.pack()

startbutton = Button(root, text="Start Process")
startbutton.pack()

pathlabel = Label(root)
pathlabel.pack()

#mainloop()
root.mainloop()
