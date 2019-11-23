from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog

wind = Tk()
wind.title("Welcome to our Colorization Tool")
wind.geometry("800x500")
wind.configure(background = "light blue")

def browsefunc():
    filename = filedialog.askopenfilename()
    pathlabel.config(text=filename)


#L = Label(wind, image = "image2.jpg")
browsebutton = Button(wind, text="Browse", command=browsefunc)
browsebutton.pack()
pathlabel = Label(wind)
pathlabel.pack()

wind.mainloop()