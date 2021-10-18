from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()
root.title('Coding With Doc')

root.filename = filedialog.askopenfilename(initialdir="Desktop", title="select a file",filetypes=("png", "*.png"))


mainloop()