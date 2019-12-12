from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog
      
window = Tk() 
menu = Menu(window) 

def browsefunc():
    filename = filedialog.askopenfilename()
    pathlabel.config(text=filename)
    #canvas = Canvas(width=300, height=200, bg='light blue')
    load = Image.open(filename) 
    img = ImageTk.PhotoImage(file = filename)
    #canvas.create_image(20, 20, anchor=NW, image = img)
    #canvas.pack()

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