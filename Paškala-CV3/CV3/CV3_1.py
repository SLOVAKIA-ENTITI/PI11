import tkinter
import random
canvas = tkinter.Canvas(height=1000, width=1000)
canvas.pack()


x=10
xx = x
y=10
pt1=int(input("Zadaj počet riadkov:"))
pt2=int(input("Zadaj počet stĺpcov:"))
d=30
m=3
farba1 = "gold"
farba2="maroon"
for i in range(pt1):
    for j in range(pt2):
        x = x+d+m
        canvas.create_rectangle(x,y,x+d,y+d, fill = farba1)
        if i % 2 == 0:
            farba1, farba2 = farba2, farba1
        else:
            farba2,farba1=farba1,farba2
    y = y+d+m
    x=xx



canvas.mainloop()