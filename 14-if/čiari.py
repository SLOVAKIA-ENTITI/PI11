import tkinter
canvas_width = 1000
canvas_height = 1000
canvas = tkinter.Canvas(height = canvas_height, width = canvas_width)
canvas.pack()

mz = 40
x = 10
y = 10
z = 10
q = 10
x1 = x
y1 = y
hrúbka = 20
farba1, farba2 = "red", "blue"
for i in range(canvas_width // mz):
    canvas.create_line(x, y, x, y+990, width=hrúbka, fill=farba1)
    x = x + mz
    farba1, farba2 = farba2, farba1
for j in range(canvas_height // mz):
    canvas.create_line(z, q, z+990, q, width=hrúbka, fill=farba1)
    q = q + mz
    farba1, farba2 = farba2, farba1


canvas.mainloop()