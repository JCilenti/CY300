import tkinter as tk
from PIL import ImageTk, Image
from tkinter import filedialog
from PIL import Image


#This creates the main window of an application
window = tk.Tk()
window.title("Join")
window.geometry("300x300")
window.configure(background='grey')

path = filedialog.askopenfilename()

#Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
img = ImageTk.PhotoImage(Image.open(path))

#The Label widget is a standard Tkinter widget used to display a text or image on the screen.
panel = tk.Label(window, image = img)

#The Pack geometry manager packs widgets in rows or columns.
panel.pack(side = "bottom", fill = "both", expand = "yes")

# This is where I add in the code for pixel values
f = open("PIXVALS.txt", "w")
img = Image.open(path)
pix_val = list(img.getdata())
pix_val_flat = [x for sets in pix_val for x in sets]
f.write(str(pix_val_flat))

#Start the GUI
window.mainloop()
##############################################################################################
'''
import tkinter as tk
from tkinter import filedialog

def UploadAction(event=None):
    filename = filedialog.askopenfilename()
    print('Selected:', filename)

root = tk.Tk()
button = tk.Button(root, text='Open', command=UploadAction)
button.pack()

root.mainloop()
'''
'''
from tkinter import *
from tkinter import filedialog
window = Tk()
window.title("Please Select the Image you Would Like to Colorize")
window.geometry('350x200')
file = filedialog.askopenfilename(filetypes = (("Image files", "*.jpg"),("all files","*.*")))
dir = filedialog.askdirectory()
'''
'''
lbl = Label(window, text = "Hello")
lbl.grid(column = 0, row = 0)
def clicked():
    lbl.configure(text = "Button was clicked !!")
btn = Button(window, text = "Click Me", command = clicked)
btn.grid(column = 1, row = 0)
window.mainloop()
'''