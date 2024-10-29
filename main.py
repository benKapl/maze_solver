from graphics import Window
from lines import Point, Line

def main():
    win = Window(800, 600)

    x1 = Point(10, 10)
    y1 = Point(100, 100)

    x2 = Point(300, 40)
    y2 = Point(200, 500)

    line1 = Line(x1, y1)
    line2 = Line(x2, y2)

    win.draw_line(line1, "red")
    win.draw_line(line2, "blue")

    win.wait_for_close()

if __name__ == "__main__":
    main()