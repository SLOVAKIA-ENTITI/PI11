import tkinter

canvas = tkinter.Canvas(height=1000, width=1000)
canvas.pack()
x = 10
y = 10
d = 5
f = "lightblue"
pocet = 995 // d



for i in range(pocet):
    for j in range(pocet):
        #M
        canvas.create_rectangle(x, y, x+d, y+d, fill = f)
        canvas.create_rectangle(x, y+d, x+d, y+2*d, fill = f)
        canvas.create_rectangle(x, y+2*d, x+d, y+3*d, fill = f)
        canvas.create_rectangle(x, y+3*d, x+d, y+4*d, fill = f)
        canvas.create_rectangle(x, y+4*d, x+d, y+5*d, fill = f)
        canvas.create_rectangle(x, y+5*d, x+d, y+6*d, fill = f)
        canvas.create_rectangle(x, y+6*d, x+d, y+7*d, fill = f)
        canvas.create_rectangle(x+d, y+d, x+2*d, y+2*d, fill = f)
        canvas.create_rectangle(x+2*d, y+2*d, x+3*d, y+3*d, fill = f)
        canvas.create_rectangle(x+2*d, y+3*d, x+3*d, y+4*d, fill = f)
        canvas.create_rectangle(x+3*d, y+d, x+4*d, y+2*d, fill = f)
        canvas.create_rectangle(x+4*d, y, x+5*d, y+d, fill = f)
        canvas.create_rectangle(x+4*d, y+d, x+5*d, y+2*d, fill = f)
        canvas.create_rectangle(x+4*d, y+2*d, x+5*d, y+3*d, fill = f)
        canvas.create_rectangle(x+4*d, y+3*d, x+5*d, y+4*d, fill = f)
        canvas.create_rectangle(x+4*d, y+4*d, x+5*d, y+5*d, fill = f)
        canvas.create_rectangle(x+4*d, y+5*d, x+5*d, y+6*d, fill = f)
        canvas.create_rectangle(x+4*d, y+6*d, x+5*d, y+7*d, fill = f)

        x = 9*d
        f = "cyan"
        #A
        canvas.create_rectangle(x, y+6*d, x+d, y+7*d, fill = f)
        canvas.create_rectangle(x, y+5*d, x+d, y+6*d, fill = f)
        canvas.create_rectangle(x, y+4*d, x+d, y+5*d, fill = f)
        canvas.create_rectangle(x, y+3*d, x+d, y+4*d, fill = f)
        canvas.create_rectangle(x, y+2*d, x+d, y+3*d, fill = f)
        canvas.create_rectangle(x, y+d, x+d, y+2*d, fill = f)
        canvas.create_rectangle(x+d, y, x+2*d, y+d, fill = f)
        canvas.create_rectangle(x+2*d, y, x+3*d, y+d, fill = f)
        canvas.create_rectangle(x+3*d, y, x+4*d, y+d, fill = f)
        canvas.create_rectangle(x+4*d, y+d, x+5*d, y+2*d, fill = f)
        canvas.create_rectangle(x+4*d, y+2*d, x+5*d, y+3*d, fill = f)
        canvas.create_rectangle(x+4*d, y+3*d, x+5*d, y+4*d, fill = f)
        canvas.create_rectangle(x+4*d, y+4*d, x+5*d, y+5*d, fill =f)
        canvas.create_rectangle(x+4*d, y+5*d, x+5*d, y+6*d, fill = f)
        canvas.create_rectangle(x+4*d, y+6*d, x+5*d, y+7*d, fill = f)
        canvas.create_rectangle(x+2*d, y+3*d, x+3*d, y+4*d, fill = f)
        canvas.create_rectangle(x+d, y+3*d, x+2*d, y+4*d, fill = f)
        canvas.create_rectangle(x+3*d, y+3*d, x+4*d, y+4*d, fill =f)

        x = 16*d
        f = "blue"
        #T
        canvas.create_rectangle(x, y, x+d, y+d, fill = f)
        canvas.create_rectangle(x+d, y, x+2*d, y+d, fill = f)
        canvas.create_rectangle(x+2*d, y, x+3*d, y+d, fill = f)
        canvas.create_rectangle(x+3*d, y, x+4*d, y+d, fill = f)
        canvas.create_rectangle(x+4*d, y, x+5*d, y+d, fill = f)
        canvas. create_rectangle(x+2*d, y+d, x+3*d, y+2*d, fill = f)
        canvas.create_rectangle(x+2*d, y+2*d, x+3*d, y+3*d, fill = f)
        canvas.create_rectangle(x+2*d, y+3*d, x+3*d, y+4*d, fill = f)
        canvas.create_rectangle(x+2*d, y+4*d, x+3*d, y+5*d, fill = f)
        canvas.create_rectangle(x+2*d, y+5*d, x+3*d, y+6*d, fill = f)
        canvas.create_rectangle(x+2*d, y+6*d, x+3*d, y+7*d, fill = f)

        x = 23*d
        f = "red"
        #U
        canvas.create_rectangle(x, y, x+d, y+d, fill = f)
        canvas.create_rectangle(x, y+d, x+d, y+2*d, fill = f)
        canvas.create_rectangle(x, y+2*d, x+d, y+3*d, fill = f)
        canvas.create_rectangle(x, y+3*d, x+d, y+4*d, fill = f)
        canvas.create_rectangle(x, y+4*d, x+d, y+5*d, fill = f)
        canvas.create_rectangle(x, y+5*d, x+d, y+6*d, fill = f)
        canvas.create_rectangle(x+d, y+6*d, x+2*d, y+7*d, fill = f)
        canvas.create_rectangle(x+2*d, y+6*d, x+3*d, y+7*d, fill = f)
        canvas.create_rectangle(x+3*d, y+6*d, x+4*d, y+7*d, fill = f)
        canvas.create_rectangle(x+4*d, y+5*d, x+5*d, y+6*d, fill = f)
        canvas.create_rectangle(x+4*d, y+4*d, x+5*d, y+5*d, fill = f)
        canvas.create_rectangle(x+4*d, y+3*d, x+5*d, y+4*d, fill =f)
        canvas.create_rectangle(x+4*d, y+2*d, x+5*d, y+3*d, fill = f)
        canvas.create_rectangle(x+4*d, y+d, x+5*d, y+2*d, fill = f)
        canvas.create_rectangle(x+4*d, y, x+5*d, y+d, fill = f)

        x = 30*d
        f = "lime"
        #S
        canvas.create_rectangle(x+d, y, x+2*d, y+d, fill = f)
        canvas.create_rectangle(x+2*d, y, x+3*d, y+d, fill = f)
        canvas.create_rectangle(x+3*d, y, x+4*d, y+d, fill = f)
        canvas.create_rectangle(x+4*d, y, x+5*d, y+d, fill = f)
        canvas.create_rectangle(x, y+d, x+d, y+2*d, fill = f)
        canvas.create_rectangle(x, y+2*d, x+d, y+3*d, fill = f)
        canvas.create_rectangle(x+d, y+3*d, x+2*d, y+4*d, fill = f)
        canvas.create_rectangle(x+2*d, y+3*d, x+3*d, y+4*d, fill = f)
        canvas.create_rectangle(x+3*d, y+3*d, x+4*d, y+4*d, fill = f)
        canvas.create_rectangle(x+4*d, y+4*d, x+5*d, y+5*d, fill = f)
        canvas.create_rectangle(x+4*d, y+5*d, x+5*d, y+6*d, fill = f)
        canvas.create_rectangle(x+3*d, y+6*d, x+4*d, y+7*d, fill = f)
        canvas.create_rectangle(x+2*d, y+6*d, x+3*d, y+7*d, fill = f)
        canvas.create_rectangle(x+d, y+6*d, x+2*d, y+7*d, fill = f)
        canvas.create_rectangle(x, y+6*d, x+d, y+7*d, fill = f)







canvas.mainloop()