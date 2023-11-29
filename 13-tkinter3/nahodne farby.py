import tkinter
import random

canvas=tkinter.Canvas(height=500, width=500)
canvas.pack()

meno = "Ján"
priezvisko = "Mrkvička"
vek = 255

print("Volám sa ", meno," ", priezvisko, "a mám ", vek, ".")
print(f"Volám sa {meno} {priezvisko} a mám {vek:02x} rokov.")  # x prevedie číslo do šestnástkovej {hexadecimálnej} sústavy


r = 5
for i in range(200):
    x = random.randint(2, 480)
    y = random.randint(2, 480)
    f = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    farba = f"#{f:02x}{g:02x}{b:02x}"
    canvas.create_oval(x-r, y-r, x + r, y + r, fill=farba)

canvas.mainloop()