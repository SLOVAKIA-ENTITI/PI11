import tkinter
import random
canvas_width = 300
canvas_height = 300
pocet = 10000
polomer = 10
canvas = tkinter.Canvas(height=canvas_height, width=canvas_width)
canvas.pack()


for i in range(pocet):
    x = random.randint(polomer + 2, canvas_width - polomer - 2)
    y = random.randint(polomer + 2, canvas_height - polomer - 2)
    if x <= canvas_width // 2 and y <= canvas_height // 2:
        farba = "red"
    elif x > canvas_width // 2 and y <= canvas_height // 2:
        farba = "lime"
    elif x <= canvas_width // 2 and y > canvas_height // 2:
        farba = "blue"
    elif x > canvas_width // 2 and y > canvas_height // 2:
        farba = "yellow"
    else:
        pass
    canvas.create_oval(x + polomer // 2, y + polomer // 2, x - polomer // 2, y - polomer // 2, fill = farba , width = 0)

canvas.mainloop()