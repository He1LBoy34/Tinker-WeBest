from tkinter import *

root = Tk()  # базовое окно нашего приложения

the_label = Label(root, text='It is all very simple')  # виджет с текстом
the_label.pack()    # отображение в главном окне

root.mainloop()  # зацикливание приложения
