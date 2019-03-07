from tkinter import *

def output(event):
    txt = entry_1.get()
    try:
        if int(txt) < 18:
            label1["text"] = "it's too early for you here"
        else:
            label1["text"] = "Welcome"
    except ValueError:
        label1["text"] = 'Enter the correct age'

root = Tk()  # базовое окно нашего приложения
root.title('How old are you?')

entry_1 = Entry(root, width=10, font=15)
button1 = Button(root, text="check")
label1 = Label(root, width=27, font=15)

entry_1.grid(row=0, column=0)
button1.grid(row=0, column=1)
label1.grid(row=0, column=2)

button1.bind("<Button-1>", output)

root.mainloop()  # зацикливание приложения
