import tkinter as tk
from tkinter import filedialog, Menu
from PIL import Image, ImageTk

def openFile():
    filePath = filedialog.askopenfilename(filetypes=[("TIFF files", "*.tif"), ("TIFF files", "*.tiff")])
    if filePath:
        # load chosen image
        img = Image.open(filePath)
        
        # adjust canvas for image specs
        canvas.config(width=img.width, height=img.height)
        
        # convert image to Tkinter format
        imgTk = ImageTk.PhotoImage(img)
        
        # clear canvas 
        canvas.delete("all")
        
        # show image 
        canvas.create_image(0, 0, anchor='nw', image=imgTk)
        
        canvas.image = imgTk

def exitProgram():
    root.destroy()

# setting up the main window
root = tk.Tk()
root.title("TIFF Viewer")

# making a menu bar
menuBar = Menu(root)
fileMenu = Menu(menuBar, tearoff=0)
fileMenu.add_command(label="Open File", command=openFile) 
fileMenu.add_command(label="Exit", command=exitProgram) 
menuBar.add_cascade(label="File", menu=fileMenu)
root.config(menu=menuBar)

# a canvas where the images will show up
canvas = tk.Canvas(root, width=704, height=576)
canvas.pack()

root.mainloop()
