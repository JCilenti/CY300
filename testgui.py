from tkinter import *
from tkinter import filedialog

root = Tk()
root.title("Welcome to Our Colorization Tool")
root.geometry("500x500")
root.configure(background='light blue')

def browsefunc():
    filename = filedialog.askopenfilename()
    pathlabel.config(text=filename)

browsebutton = Button(root, text="Browse", command=browsefunc)
browsebutton.pack()

pathlabel = Label(root)
pathlabel.pack()

#mainloop()

root.mainloop()
