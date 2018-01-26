from Tkinter import Tk, Canvas, Frame, BOTH
from collections import namedtuple

Point = namedtuple("point", "x y")

root = Tk()
r_w = 300
r_h = 300
root_mid = Point(r_w / 2, r_h / 2)
root.geometry(str(r_w) + "x" + str(r_h))

debug = 0


def draw_face(d):
    frame = Frame(root)
    frame.master.title("Face")
    frame.pack(fill=BOTH, expand=1)
    canvas = Canvas(frame)
    top_point = Point(root_mid.x - d, root_mid.y - d)
    bot_point = Point(root_mid.x + d, root_mid.y + d)
    draw_oval(canvas, top_point.x, top_point.y, bot_point.x, bot_point.y)
    draw_eye(canvas, root_mid.x - d * .5, root_mid.y - d * .22, d * .15)
    draw_eye(canvas, root_mid.x + d * .5, root_mid.y - d * .22, d * .15)
    draw_nose(canvas, d * .20)
    draw_mouth(canvas, root_mid.x, root_mid.y + d * .40, d * .20)
    canvas.pack(fill=BOTH, expand=1)
    frame.pack(fill=BOTH, expand=1)
    root.mainloop()


def draw_oval(canvas, x1, y1, x2, y2):
    canvas.create_oval(x1, y1, x2, y2)
    if debug:
        canvas.create_oval(x1, y1, x1, y1)
        canvas.create_oval(x2, y2, x2, y2)


def draw_eye(canvas, x, y, d):
    p_1 = Point(x - d, y - d)
    p_2 = Point(x + d, y + d)
    draw_oval(canvas, p_1.x, p_1.y, p_2.x, p_2.y)


def draw_nose(canvas, size):
    p_1 = Point(root_mid.x - size * .50, root_mid.y + size * .75)
    p_2 = Point(root_mid.x, root_mid.y + size * .75)
    p_3 = Point(root_mid.x, root_mid.y - size)
    points = [p_1.x, p_1.y, p_2.x, p_2.y, p_3.x, p_3.y]
    canvas.create_polygon(points)


def draw_mouth(canvas, x, y, d):
    p_1 = Point(x - d, y - d)
    p_2 = Point(x + d, y + d)
    canvas.create_arc(p_1.x, p_1.y, p_2.x, p_2.y, start=-180,
                      extent=180)


draw_face(80)
