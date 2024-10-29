from tkinter import Canvas

class Point():
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

class Line():
    def __init__(self, a: Point, b: Point) -> None:
        self.__a = a
        self.__b = b

    def draw(self, canvas: Canvas, fill_color: str):
        canvas.create_line(
            self.__a.x,  #x1
            self.__a.y,  #y1
            self.__b.x,  #x2
            self.__b.y,  #y2
            fill=fill_color,
            width=2
        )

