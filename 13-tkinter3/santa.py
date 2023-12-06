import tkinter
import time
import random

canvas_width = 400
canvas_height = 600
santa_x = canvas_width // 2
santa_y = 66
santa_posun = 1

santa_2x = canvas_width // 5
santa_2y = 544
santa_posun2 = -1

canvas = tkinter.Canvas(width=canvas_width, height=canvas_height)
canvas.pack()


image_santa = tkinter.PhotoImage(file="santa (2).png")
santa = canvas.create_image(santa_x, santa_y, image = image_santa)
while True:
    canvas.update()
    time.sleep(0.000000001)
    canvas.move(santa, 0, santa_posun)
    santa_y = santa_y + santa_posun
    if santa_y == canvas_height + 64:
        canvas.delete(santa)
        santa_y = 66
        santa = canvas.create_image(santa_x, santa_y, image=image_santa)

image_santa2 = tkinter.PhotoImage(file="santa (2).png")
santa2 = canvas.create_image(santa_2x, santa_2y, image = image_santa2)
while True:
    canvas.update()
    time.sleep(0.000001)
    canvas.move(santa2, 0, santa_posun2)
    santa_2y = santa_2y + santa_posun2
    if santa_2y == canvas_height + 608:
        canvas.delete(santa2)
        santa_2y = 544
        santa2 = canvas.create_image(santa2x, santa_2y, image = image_santa2)