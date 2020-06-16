from tkinter import *
root = Tk()
canvas = Canvas(root, width=700, height=700)
canvas.focus_set()
canvas.pack()
def draw_evil_smile(x1, y1, x2, y2):
    pass
canvas.create_oval(200, 200, 500, 500, fill="yellow")
canvas.create_oval(250, 250, 290, 290, fill="black")
canvas.create_oval(260, 260, 270, 270, fill="red")
canvas.create_oval(430, 240, 440, 290, fill="black")
canvas.create_oval(430, 250, 440, 270, fill="red")
root.mainloop()
