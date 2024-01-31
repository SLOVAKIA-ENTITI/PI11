import tkinter
canvas = tkinter.Canvas(width=1000, height=1000)
canvas.pack()

def rgb(r, g, b):
    return f"#{r:02x}{g:02x}{b:02x}"
def stvorce(x, y, pt, d, r=255, g=255, b=255):
    for j in range(pt):
        spektrum = 255 // pt
        canvas.create_rectangle(x, y, x+d, y+d, fill=rgb(r, g, b))
        x += d
        if r > spektrum:
            r -=spektrum
        if g > spektrum:
            g -=spektrum
        if b > spektrum:
            b -=spektrum






stvorce(20,20,20,20,255,0,0)
stvorce(20,40,20,20,0,255,0)
stvorce(20,60,20,20,0,0,255)








canvas.mainloop()