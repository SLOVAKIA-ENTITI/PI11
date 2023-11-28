import tkinter

canvas = tkinter.Canvas(height=500, width=500)
canvas.pack()


d = 20
f1 = "red"
fo1 = "black"
f2 = "grey"
fo2 = "black"
f3 = "cyan"
fo3 = "brown"
pocet = 498 // d


for y in range(pocet):
    for x in range(pocet):
        x = x + d
        canvas.create_polygon(x, y+d, x+d//2, y, x+d, y+d, fill = f1, outline = fo1)
        canvas.create_rectangle(x, y+d, x+d, y+d*2, fill = f2, outline = fo2 )
        canvas.create_rectangle(x+d*1//4, y+d*1//4+d, x+d*3//4, y+d*3//4+d, fill = f3, outline = fo3)
        canvas.create_line(x+d*1//4, y+d*2//4+d, x+d*3//4, y+d*2//4+d, fill = fo3)
        canvas.create_line(x+d//2, y+d*1//4+d, x+d//2, y+d*3//4+d, fill= fo3)





    #opakovanie



canvas.mainloop()