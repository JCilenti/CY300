from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog

window = Tk()
window.configure(background='light blue')
window.title("Welcome to Our Colorization Tool")
window.geometry("500x500")



def browsefunc():
    filename = filedialog.askopenfilename()
    pathlabel.config(text=filename)
    canvas = Canvas(window)
    img = ImageTk.PhotoImage(file = filename)
    print(img)
    canvas.create_image(20, 20, anchor=NW, image = img)
    canvas.pack()
    # look for a .draw function

browsebutton = Button(window, text="Browse", command=browsefunc)
browsebutton.pack()

startbutton = Button(window, text="Start Process")
startbutton.pack()

pathlabel = Label(window)
pathlabel.pack()

#mainloop()
mainloop()
