from tkinter import Tk, BOTH, Canvas


class Point():
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y


class Line():
    def __init__(self, p1: Point, p2: Point) -> None:
        self.p1 = p1
        self.p2 = p2

    def draw(self, canvas: Canvas, fill_color="black"):
        canvas.create_line(
            self.p1.x,  #x1
            self.p1.y,  #y1
            self.p2.x,  #x2
            self.p2.y,  #y2
            fill=fill_color,
            width=2
        )


class Cell():
    def __init__(self, x1, x2, y1, y2) -> None:
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__x1 = x1
        self.__x2 = x2
        self.__y1 = y1
        self.__y2 = y2

    def draw(self, canvas: Canvas, fill_color="black"):
        if self.has_left_wall:
            canvas.create_line(
                self.__x1,  #x1
                self.__x1,  #y1
                self.__y1,  #x2
                self.__y2,  #y2
                fill=fill_color,
                width=2
            )
        if self.has_right_wall:
            canvas.create_line(
                self.__x2,  #x1
                self.__y1,  #y1
                self.__x2,  #x2
                self.__y2,  #y2
                fill=fill_color,
                width=2
            )
        if self.has_top_wall:
            canvas.create_line(
                self.__x1,  #x1
                self.__y1,  #y1
                self.__x2,  #x2
                self.__y1,  #y2
                fill=fill_color,
                width=2
            )
        if self.has_bottom_wall:
            canvas.create_line(
                self.__x1,  #x1
                self.__y2,  #y1
                self.__x2,  #x2
                self.__y2,  #y2
                fill=fill_color,
                width=2
            )


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

    def draw_line(self, line: Line, fill_color="black"):
        line.draw(self.__canvas, fill_color)

    def draw_cell(self, cell: Cell, fill_color="black"):
        cell.draw(self.__canvas, fill_color)

    def close(self):
        self.__running = False