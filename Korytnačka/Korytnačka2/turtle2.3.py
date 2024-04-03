import turtle
turtle.delay(0)


t1=turtle.Turtle()
t2=turtle.Turtle()
t3=turtle.Turtle()
t1.penup()
t1.setpos(-100,0)
t1.pendown()
t2.penup()
t2.setpos(100,0)
t2.pendown()
t3.penup()
t3.setpos(0,-100)
t3.pendown()

uhol=360

for j in range(uhol):
    for i in range(4):
        t1.fd(50)
        t2.fd(50)
        t1.lt(90)
        t2.lt(90)
        t3.fd(50)
        t3.lt(90)
    t1.lt(360//uhol)
    t2.lt(360//uhol)
    t3.lt(360//uhol)








turtle.mainloop()