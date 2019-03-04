from tkinter import *

root = Tk()  # базовое окно нашего приложения

top_frame = Frame(root)  # контейнер
top_frame.pack()    # метод пек без параметров по умолчанию размещает виджет вверху

bottom_frame = Frame(root)  # второй контейнер
bottom_frame.pack(side=BOTTOM)  # место размещения второго контейнера

button1 = Button(top_frame, text="Button 1", fg="green")
button2 = Button(top_frame, text="Button 2", fg="blue")
button3 = Button(top_frame, text="Button 3", fg="red")
button4 = Button(bottom_frame, text="Button 4", fg="white")

button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=BOTTOM)

root.mainloop()  # зацикливание приложения нужно в любом случае
