import turtle

t = turtle.Turtle()
turtle.delay(0)
uhol = 50



def obluk(d):
    for i in range(9):
        t.fd(d)             #dĺžka
        t.lt(10)            #otočenie v stupňoch


def lupen(d):
    for i in range(2):
        obluk(d)            #prenesenie funkcie
        t.lt(90)           #otocenie


def kvet(d):
    for i in range(360//uhol):
        lupen(d)
        t.left(uhol)