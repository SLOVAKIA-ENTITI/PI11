import tkinter
canvas_width = 1000
canvas_height = 1000
canvas = tkinter.Canvas(height = canvas_height, width = canvas_width)
canvas.pack()
polomer = 10
pocet = canvas_width // (polomer * 2)

for i in range(pocet):
    for j in range(pocet):
        x = j*polomer * 2 + 10
        y = i*polomer * 2 + 10
        if j ==  pocet // 2:
            farba = 'red'
        else:
            farba = 'white'
        canvas.create_oval(x - 8, y - 8, x + 8, y + 8, fill=farba)


canvas.mainloop()