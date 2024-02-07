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



x=20
y=20
pt=50
d=20
yy=y
fg=5
mg=1
for j in range(fg):
    for i in range(mg):
        stvorce(x,y,pt,d,255,0,0)
        stvorce(x,y+d,pt,d,0,255,0)
        stvorce(x,y+d*2,pt,d,0,0,255)
    y = y + 60







canvas.mainloop()