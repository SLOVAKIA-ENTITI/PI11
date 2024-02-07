import tkinter
import random
canvas = tkinter.Canvas()
canvas.pack()

def karticka(x,y,text):
    canvas.create_rectangle(x-50,y-20,x+50,y+20,fill = "light grey")
    canvas.create_text(x,y,text=text, font = "arial 14")



for i in range(10):
    karticka(x=random.randint(50,300),y=random.randrange(50,200),text="Python")

canvas.mainloop()