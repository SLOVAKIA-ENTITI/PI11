import tkinter
import random
canvas = tkinter.Canvas()
canvas.pack()
p=5

for i in range(10000):
    a = random.randint(10,350)
    b = random.randint(10,250)
    if b<90:
        canvas.create_oval(a-p,b-p,a+p,b+p, fill = "black", outline="")
    elif b<170:
        canvas.create_oval(a-p,b-p,a+p,b+p, fill = "red", outline="")
    else:
        canvas.create_oval(a-p,b-p,a+p,b+p, fill = "gold", outline="")
canvas.mainloop()