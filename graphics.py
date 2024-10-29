from tkinter import Tk, BOTH, Canvas

from lines import Line


class Window():
    def __init__(self, width, height) -> None:
        # Create root
        self.__root = Tk()
        self.__root.title("Maze Solver")
        # Create canvas
        self.__canvas = Canvas(self.__root, bg="white", height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand=1) # geometry manager
        # 
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update()
        self.__root.update_idletasks()
    
    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()

    def close(self):
        self.__running = False

    def draw_line(self, line: Line, fill_color):
        line.draw(self.__canvas, fill_color)


# class Point():
#     def __init__(self, x: int, y: int) -> None:
#         self.x = x
#         self.y = y


# class Line():
#     def __init__(self, a: Point, b: Point) -> None:
#         self.__a = a
#         self.__b = b

#     def draw(self, canvas: Canvas, fill_color: str):
#         canvas.create_line(
#             self.__a.x,  #x1
#             self.__a.y,  #y1
#             self.__b.x,  #x2
#             self.__b.y,  #y2
#             fill=fill_color,
#             width=2
#         )