import tkinter as tk
from PIL import ImageTk,Image
from tkinter import filedialog
      
window = tk.Tk() 
window.geometry("400x300")
menu = tk.Menu(window) 

def browsefunc():
    filename = filedialog.askopenfilename()
    print(filename)
    pathlabel.config(text=filename)
    canvas = tk.Canvas(width=300, height=200)
    load = Image.open(filename) 
    img = ImageTk.PhotoImage(file = filename)
    canvas.create_image(20, 20, anchor=NW, image = img)
    canvas.pack()

pathlabel = tk.Label(window)
pathlabel.pack()

def About_func():
    T = tk.Text(window, height = 16, width = 45)
    T.pack()
    T.insert(tk.END, "Welcome to our Colorization Tool\nThe process is very easy.\nSimply select File -> Open and the image\nfile you would like to colorize\nFrom there, our algorithm will run\nand your image will be done in no time.\n\n\n           ##### ENJOY!!! #####")

def callback():
    print("Clicked")

window.config(menu=menu) 
filemenu = tk.Menu(menu) 
menu.add_cascade(label='File', menu=filemenu) 
filemenu.add_command(label='Open...', command=browsefunc) 
filemenu.add_separator() 
filemenu.add_command(label='Start Process', command=callback)
filemenu.add_command(label='Exit', command=window.quit) 
helpmenu = tk.Menu(menu) 
menu.add_cascade(label='Help', menu=helpmenu) 
helpmenu.add_command(label='About', command=About_func) 
tk.mainloop() 