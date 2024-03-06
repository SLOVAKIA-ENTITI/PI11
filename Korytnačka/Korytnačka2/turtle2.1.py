import random
import turtle
import random
t = turtle.Turtle()
turtle.delay(0)
uhol = 40



def obluk(d):
    for i in range(9):
        t.fd(d)             #dĺžka
        t.lt(10)            #otočenie v stupňoch


def lupen(d):
    for i in range(2):
        obluk(d)            #prenesenie funkcie
        t.lt(90)           #otocenie

def rgb(r, g, b):
    return f"#{r:02x}{g:02x}{b:02x}"

def kvet(d,r=255, g=255, b=255):
    for i in range(360 // uhol):
        t.pendown()
        t.fillcolor(f"#{r:02x}{g:02x}{b:02x}")
        t.begin_fill()
        lupen(d)
        t.end_fill()
        t.left(uhol)
        t.penup()




for i in range(10):
    kvet(10,)
    x=random.randrange(-300,300)
    y=random.randrange(-300, 300)
    t.setpos(x,y)








turtle.mainloop()