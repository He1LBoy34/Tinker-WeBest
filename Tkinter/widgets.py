from tkinter import *

root = Tk()  # базовое окно нашего приложения

one = Label(root, text='One', bg='white', fg='black')
one.pack()

one = Label(root, text='Two', bg='white', fg='black')
one.pack()

one = Label(root, text='Three', bg='white', fg='black')
one.pack()

root.mainloop()  # зацикливание приложения
