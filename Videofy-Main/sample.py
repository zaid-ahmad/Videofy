from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry('500x300')

# Create a main frame
main_frame = Frame(root)
main_frame.pack(fill=BOTH, expand=1)

# Create a canvas
my_canvas = Canvas(main_frame)
my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

# Add a scollbar to the canvas
my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
my_scrollbar.pack(side=RIGHT, fill=Y)

# Configure the canvas
my_canvas.configure(yscrollcommand=my_scrollbar.set)
my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))

# Create another frame inside canvas 
second_frame = Frame(my_canvas)

# Add that new frame to a window in the canvas
my_canvas.create_window((0,0), window=second_frame, anchor="nw")

for thing in range(100):
    Button(second_frame, text=f'Button {thing}').grid(row=thing, column=0, pady=10, padx=10)

root.mainloop()