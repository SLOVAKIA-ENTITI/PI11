import tkinter

canvas = tkinter.Canvas(height=1000, width=1000)
canvas.pack()
polomer = 10
pocet = 13
for i in range(pocet):
    for j in range(pocet):
        x = j*polomer * 2
        y = i*polomer * 2
        if j ==  pocet // 2:
            farba = 'red'
        else:
            farba = 'white'
        canvas.create_oval(x - 8, y - 8, x + 8, y + 8, fill=farba)


canvas.mainloop()