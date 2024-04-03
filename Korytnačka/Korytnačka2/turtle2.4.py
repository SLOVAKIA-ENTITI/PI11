import turtle

pocet = 4
turtle.delay(0)
turtles = []   #list(resp.pole) korytnačiek


for i in range(pocet):
    t = turtle.Turtle()
    t.penup()
    t.setpos(i * 100,0)
    t.pendown()
    turtles.append(t)

#for i in range(4):
#    for t in turtles:
#        t.fd(50)
#        t.rt(90)

uhol=20
for j in range(uhol):
    for t in turtles:
        for i in range(4):
            t.fd(50)
            t.rt(90)
        t.rt(uhol)
turtle.mainloop()