import tkinter
import time
import random
canvas = tkinter.Canvas()
canvas.pack()

stvorec1 = canvas.create_rectangle(10, 10 , 110, 110, fill = "blue")
for i in range(1000):
    canvas.update()
    time.sleep(0.1)
    canvas.move(stvorec1, 1, 0)         # stvorec1 je objekt ktorý sa bude posúvať, 100 je o koľko posunúť na x-ovej osy a 0 o koľko na y-onovej osy
    farba = random.choice (("red", "blue"))
    canvas.itemconfig(stvorec1, fill = farba)



canvas.mainloop()