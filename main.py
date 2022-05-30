from tkinter import *
import tkinter.ttk as ttk

root = Tk()

root.geometry("500x550")

root.attributes('-alpha', 0.7)

my_label = Label(root, text="Hello World!", font=("Helvetica", 20))
my_label.pack(pady=20)

def slide(x):
	root.attributes('-alpha', my_slider.get())
	slide_label.config(text=str(round(my_slider.get(), 2)))

my_slider = ttk.Scale(root, from_=0.1, to=1.0, value=0.7, orient=HORIZONTAL, command=slide)
my_slider.pack(pady=20) 

slide_label = Label(root, text='')
slide_label.pack(pady=10)

def make_solid(e):
	new.attributes('-alpha', 1.0)

def new_window():
	global new
	new = Toplevel()
	new.attributes('-alpha', 0.5)
	new.bind("<Button-1>", make_solid)

new_window = Button(root, text="New Window", command=new_window)
new_window.pack(pady=20)


root.mainloop()
