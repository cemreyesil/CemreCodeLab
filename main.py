from tkinter import Label, Tk, Entry, Button
from str_to_no import stringtonumber

root = Tk() # create root window

root.title("String to Number")
root.geometry('420x260')

# Adding a label to the root window
lbl = Label(root, 
            text = "Enter a string: ", 
            width=13, height=3, 
            compound="center",
            font=("Arial", 16, "bold"))
lbl.grid(column=0, row=0)

# Adding Entry Field
txt = Entry(root, 
            width=35)
txt.grid(column=1, row=0)

# Button is clicked
lbl2 = Label(root, 
            text = "", 
            width=13, height=3, 
            compound="center",
            font=("Arial", 16, "bold"))
lbl2.grid(column=1, row=1)
def clicked():
  number = stringtonumber(txt)
  lbl2.configure(text= number)

# Button widget with red color text
btn = Button(root, text= "Convert to Number", 
            command=clicked)

btn.grid(column=0, row=1)


root.mainloop()