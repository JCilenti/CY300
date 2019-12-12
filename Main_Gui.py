from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog
      
window = Tk() 
window.geometry("400x300")
menu = Menu(window) 

def browsefunc():
    filename = filedialog.askopenfilename()
    print(filename)
    pathlabel.config(text=filename)
    canvas = Canvas(width=300, height=200)
    load = Image.open(filename) 
    print(load)
    img = ImageTk.PhotoImage(file = filename)
    print(img)
    canvas.create_image(20, 20, anchor=NW, image = img)
    canvas.pack()

pathlabel = Label(window)
pathlabel.pack()

window.config(menu=menu) 
filemenu = Menu(menu) 
menu.add_cascade(label='File', menu=filemenu) 
filemenu.add_command(label='New') 
filemenu.add_command(label='Open...', command=browsefunc) 
filemenu.add_separator() 
filemenu.add_command(label='Exit', command=window.quit) 
helpmenu = Menu(menu) 
menu.add_cascade(label='Help', menu=helpmenu) 
helpmenu.add_command(label='About') 
mainloop() 